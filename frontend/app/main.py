"""
Frontend module for the Flask application.

This module defines a simple Flask application
that serves as the frontend for the project.
"""
# Import necessary modules and libraries
from flask import Flask, render_template
import requests
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectField


# Create a Flask web application instance
app = Flask(__name__)

# Configure the Flask app with a secret key for form security
app.config['SECRET_KEY'] = 'your_secret_key'


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


class SearchForm(FlaskForm):
    piscina_coperta = SelectField('Indoor Pool:',  choices=[('Vero', 'Si'), ('Falso', 'No')])
    sauna = SelectField('Sauna:', choices=[('Vero', 'Si'), ('Falso', 'No')])
    area_fitness = SelectField('Fitness area:',  choices=[('Vero', 'Si'), ('Falso', 'No')])
    submit = SubmitField('Search')
    
# URL of the FastAPI backend host
FASTAPI_BACKEND_HOST = 'http://backend'
# Full backend URL composed by appending '/query/' to the backend host
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


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


# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  # Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'



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
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/cerca_strutture?piscina_coperta={piscina}&sauna={sauna}&area_fitness={fitness}'
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
        return render_template("search.html", form=form, result=data_from_fastapi, error_message=error_message)
    # Render the search.html template with default values
    return render_template('search.html', form=form, result=None, error_message=error_message)

# Define a route for the Animal Crossers page
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask application on the
    # specified host and port in debug mode
    app.run(host='0.0.0.0', port=80, debug=True)






