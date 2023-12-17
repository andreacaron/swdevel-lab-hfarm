from flask import Flask, render_template, request
import requests
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


app = Flask(__name__)
# Replace with a secure secret key
app.config['SECRET_KEY'] = 'your_secret_key'

# Configuration for the FastAPI backend URL
# Replace with the actual URL of your FastAPI backend
FASTAPI_BACKEND_HOST = 'http://backend'
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class SearchForm(FlaskForm):
    piscina_coperta = SelectField('Indoor Pool:',
                                  choices=[('Vero', 'Si'), ('Falso', 'No')])
    sauna = SelectField('Sauna:', choices=[('Vero', 'Si'), ('Falso', 'No')])
    area_fitness = SelectField('Fitness area:',
                               choices=[('Vero', 'Si'), ('Falso', 'No')])
    submit = SubmitField('Search')


class QueryForm(FlaskForm):
    person_name = StringField('Person Name')
    submit = SubmitField('Submit')


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    # Fetch the date from the backend
    date_from_backend = fetch_date_from_backend()
    return render_template('index.html', date_from_backend=date_from_backend)


def fetch_date_from_backend():
    """
    Function to fetch the current date from the backend.

    Returns:
        str: Current date in ISO format.
    """
    # Adjust the URL based on your backend configuration
    backend_url = 'http://backend/get-date'
    try:
        response = requests.get(backend_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get('date', 'Date not available')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching date from backend: {e}")
        return 'Date not available'


@app.route('/search', methods=['GET', 'POST'])
def search_structure():
    # Create an instance of the SearchForm class
    form = SearchForm()
    # Initialize error_message variable
    error_message = None
    # Check if the form is submitted and valid
    if form.validate_on_submit():
        # Retrieve data from the form
        sauna = form.sauna.data
        piscina = form.piscina_coperta.data
        fitness = form.area_fitness.data
        # Construct the FastAPI backend URL with user input
        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/cerca_strutture?'
            f'piscina_coperta={piscina}&sauna={sauna}&area_fitness={fitness}'
            )

        try:
            # Make a GET request to the FastAPI backend
            response = requests.get(fastapi_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            # Parse JSON data from the FastAPI response
            data_from_fastapi, error_message = response.json(), None
        except requests.exceptions.RequestException as e:
            # Handle request exceptions and capture error message
            data_from_fastapi, error_message = None, f'Error: {str(e)}'
        # Render the search.html template with the obtained data
        return render_template("search.html",
                               form=form,
                               result=data_from_fastapi,
                               error_message=error_message)
    # Render the search.html template with default values
    return render_template('search.html',
                           form=form,
                           result=None,
                           error_message=error_message)


# Define a form class for the search form
class SearchForm(FlaskForm):
    # SelectField for choosing typology
    selected_typology = SelectField('🏠 Typology:')
    # SelectField for choosing train station with choices
    stazione = SelectField('🚅 Train station:',
                           choices=[('Vero', 'Yes'), ('Falso', 'No')])
    autostrada = SelectField('🛣 Highway:',
                           choices=[('Vero', 'Yes'), ('Falso', 'No')])
    submit = SubmitField('Search')


@app.route('/find_hotels', methods=['GET', 'POST'])
def find_hotels():
    form = SearchForm()  # Create an instance of the search form
    error_message = None
    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_typology')
    aux = json.loads(response.json())
    form.selected_typology.choices = list(aux.values())

    if form.validate_on_submit():
        selected_typology = form.selected_typology.data
        stazione = form.stazione.data
        autostrada = form.autostrada.data
        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/find_hotels_near_transports?'
            f'selected_typology={selected_typology}&stazione={stazione}&autostrada={autostrada}'
            )
        try:
            response = requests.get(fastapi_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data_from_fastapi, error_message = response.json(), None
        except requests.exceptions.RequestException as e:
            data_from_fastapi, error_message = None, f'Error: {str(e)}'

        # Render the template with the search form, result, and error message
        return render_template("find_hotels.html",
                               form=form,
                               result=data_from_fastapi,
                               error_message=error_message)

    # Render the template with the search form and no result or error message
    return render_template("find_hotels.html",
                           form=form, result=None,
                           error_message=None)


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
