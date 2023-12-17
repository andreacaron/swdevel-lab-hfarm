"""
Frontend module for the Flask application.

This module defines a simple Flask application
that serves as the frontend for the project.
"""
# Import necessary modules and libraries
from flask import Flask, render_template, request
import requests
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectField


# Create a Flask web application instance
app = Flask(__name__)

# Configure the Flask app with a secret key for form security
app.config['SECRET_KEY'] = 'your_secret_key'

# URL of the FastAPI backend host
FASTAPI_BACKEND_HOST = 'http://backend'
# Full backend URL composed by appending '/query/' to the backend host
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


# Define a form class for SearchEssentials
class SearchEssentials(FlaskForm):
    zona = SelectField('Zone:')
    ristorante = SelectField('Restaurant:', choices=[
        ('Vero', 'Yes'),
        ('Falso', 'No')
    ])
    parcheggio = SelectField('Parking', choices=[
        ('Vero', 'Yes'),
        ('Falso', 'No')
    ])
    submit = SubmitField('Search')


# Define a form class for SearhPeriferia
class SearchPeriferia(FlaskForm):
    # Field for selecting the desired type of structure
    typology = SelectField('🏠 Desired type of structure:')
    # Fields for language selection with choices
    # 'Si' for 'Vero' and 'No' for 'Falso'
    english = SelectField('🇬🇧 English language:',
                          choices=[('Vero', 'Si'), ('Falso', 'No')])
    french = SelectField('🇫🇷 French language:',
                         choices=[('Vero', 'Si'), ('Falso', 'No')])
    german = SelectField('🇩🇪 German language:',
                         choices=[('Vero', 'Si'), ('Falso', 'No')])
    spanish = SelectField('🇪🇸 Spanish language:',
                          choices=[('Vero', 'Si'), ('Falso', 'No')])
    # Submit button for the search form
    submit = SubmitField('Search')


# Define a form class for SearchForm
class SearchForm(FlaskForm):
    piscina_coperta = SelectField('Indoor Pool:',
                                  choices=[('Vero', 'Si'), ('Falso', 'No')])
    sauna = SelectField('Sauna:', choices=[('Vero', 'Si'), ('Falso', 'No')])
    area_fitness = SelectField('Fitness area:',
                               choices=[('Vero', 'Si'), ('Falso', 'No')])
    submit = SubmitField('Search')


# Define a form class for SearchTransport
class SearchTransport(FlaskForm):
    # SelectField for choosing typology
    selected_typology = SelectField('🏠 Typology:')
    # SelectField for choosing train station with choices
    stazione = SelectField('🚅 Train station:',
                           choices=[('Vero', 'Yes'), ('Falso', 'No')])

    # SelectField for choosing highway with choices
    autostrada = SelectField('🛣 Highway:',
                             choices=[('Vero', 'Yes'), ('Falso', 'No')])
    submit = SubmitField('Search')


# Define a form class for SearchExtras
class SearchExtras(FlaskForm):
    """
    Defines a search form using Flask-WTF.

    Attributes:
        aria_condizionata : SelectField for Air Conditioning input.
        animali_ammessi : SelectField for Pets Allowed input.
        submit : Submit button for the search form.
    """
    aria_condizionata_choices = [('Vero', 'Yes'), ('Falso', 'No')]
    animali_ammessi_choices = [('Vero', 'Yes'), ('Falso', 'No')]

    aria_condizionata = SelectField(
        'Air Conditioning:',
        choices=aria_condizionata_choices)
    animali_ammessi = SelectField(
        'Pets Allowed:',
        choices=animali_ammessi_choices)

    submit = SubmitField('periphery')


# Define a route for Suburbs Explorer
@app.route('/periferia', methods=['GET', 'POST'])
def search_structure_periferia():
    # Create a form instance
    form = SearchPeriferia()

    # Initialize error message
    error_message = None

    # Fetch typology choices from FastAPI backend
    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_typology')

    # Parse JSON response and set typology choices in the form
    aux = json.loads(response.json())
    form.typology.choices = list(aux.values())

    # Check if form is submitted and valid
    if form.validate_on_submit():
        # Extract form data
        typology = form.typology.data
        english = form.english.data
        french = form.french.data
        german = form.german.data
        spanish = form.spanish.data
        # Construct FastAPI backend URL with form data
        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/find_structures_suburb?'
            f'Typology={typology}&'
            f'English={english}&'
            f'French={french}&'
            f'German={german}&'
            f'Spanish={spanish}'
        )
        try:
            # Make a request to FastAPI backend
            response = requests.get(fastapi_url)
            response.raise_for_status()
            # Raise an HTTPError for bad responses
            data_from_fastapi, error_message = response.json(), None
        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            data_from_fastapi, error_message = None, f'Error: {str(e)}'

        # Render the template with the result or an error message
        return render_template("periferia.html", form=form,
                               result=data_from_fastapi,
                               error_message=error_message)

    # Render the template with the form
    return render_template('periferia.html', form=form,
                           result=None,
                           error_message=error_message)


# Define a route for the Wellness Exploratory
@app.route('/search', methods=['GET', 'POST'])
def search_structure_search():
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


# Define a route for the Animal Crossers page
@app.route('/index')
def index():
    return render_template('index.html')


# Define a route for peripherical B&b
@app.route('/periphery', methods=['GET', 'POST'])
def search_structure_periphery():
    """
    Route for handling search functionality.

    Returns:
        str: Rendered HTML content for the search page.
    """
    form = SearchExtras(request.form)
    error_message = None
    result = None

    if form.validate_on_submit():
        aria_condizionata = form.aria_condizionata.data
        animali_ammessi = form.animali_ammessi.data

        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/essential_services_periphery?'
            f'aria_condizionata={aria_condizionata}&'
            f'animali_ammessi={animali_ammessi}')

        try:
            response = requests.get(fastapi_url)

            if response.status_code == 200:
                result = response.json()
                return render_template(
                    'periphery.html',
                    form=form,
                    result=result,
                    error_message=error_message)
            else:
                error_message = 'Error fetching data from backend'

        except requests.RequestException as e:
            error_message = f'Error: {e}'

    return render_template(
        'periphery.html',
        form=form,
        result=None,
        error_message=error_message)


# Ensures route opens for peripherical B&b
@app.route('/display_results', methods=['GET'])
def display_results():
    """
    Route to display mock search results.

    Returns:
        str: Rendered HTML content for displaying search results.
    """
    result = [
        {
            'DENOMINAZIONE': 'Hotel 1',
            'PROVINCIA': 'Province 1',
            'COMUNE': 'City 1',
            'INDIRIZZO': 'Address 1',
            'NUMERO CIVICO': '123',
            'CAP': '12345',
            'EMAIL': 'hotel1@example.com',
            'TELEFONO': '+1234567890',
        },
    ]

    return render_template('results.html', result=result)


# Defining a route for Transports Exploratory
@app.route('/find_hotels', methods=['GET', 'POST'])
def find_hotels():
    form = SearchTransport()
    error_message = None
    data_from_fastapi = None

    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_typologies')
    aux = json.loads(response.json())
    form.selected_typology.choices = list(aux.values())

    if form.validate_on_submit():
        selected_typology = form.selected_typology.data
        stazione = form.stazione.data
        autostrada = form.autostrada.data
        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/find_hotels_near_transports?'
            f'selected_typology={selected_typology}&'
            f'stazione={stazione}&'
            f'autostrada={autostrada}'
        )

        try:
            response = requests.get(fastapi_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data_from_fastapi = response.json()
        except requests.exceptions.RequestException as e:
            error_message = f'Error: {str(e)}'

    return render_template(
        'find_hotels.html',
        form=form,
        result=data_from_fastapi,
        error_message=error_message
    )


# Defining a route for the Essentials
@app.route('/internal_page', methods=['GET', 'POST'])
def find():
    form = SearchEssentials()
    error_message = None
    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_zones')
    aux = json.loads(response.json())
    form.zona.choices = list(aux.values())

    if form.validate_on_submit():
        zona = form.zona.data
        ristorante = form.ristorante.data
        parcheggio = form.parcheggio.data
        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/structures?'
            f'zona={zona}&ristorante={ristorante}&parcheggio={parcheggio}'
        )
        try:
            response = requests.get(fastapi_url)
            response.raise_for_status()
            data_from_fastapi, error_message = response.json(), None
        except requests.exceptions.RequestException as e:
            data_from_fastapi, error_message = None, f'Error: {str(e)}'
# Run the Flask app
        return render_template(
            "internal_page.html",
            form=form,
            result=data_from_fastapi,
            error_message=error_message
        )

    return render_template(
        'internal_page.html',
        form=form,
        result=None,
        error_message=error_message
    )


# Define a route for the explanatory homepage
@app.route('/home_page')
def home():
    return render_template('home_page.html')


if __name__ == '__main__':
    # Run the Flask application on the
    # specified host and port in debug mode
    app.run(host='0.0.0.0', port=80, debug=True)
