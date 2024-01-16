"""
Frontend module for a Flask application.

This module defines a simple Flask application
serving as the frontend for a project.
"""

from flask import Flask, render_template, request
import requests
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
FASTAPI_BACKEND_HOST = 'http://backend'
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class SearchEssentials(FlaskForm):
    """
    Form class for searching essential services.

    Attributes:
        zone: SelectField for selecting a zone.
        restaurant: SelectField for selecting a restaurant.
        parking: SelectField for selecting parking availability.
        submit: SubmitField for initiating the search.
    """
    zone = SelectField('Zone:')
    restaurant = SelectField('Restaurant:',
                             choices=[('Vero', 'Yes'), ('Falso', 'No')])
    parking = SelectField('Parking',
                          choices=[('Vero', 'Yes'), ('Falso', 'No')])
    submit = SubmitField('Search')


class SearchPeriphery(FlaskForm):
    """
    Form class for searching structures in the periphery.

    Attributes:
        typology: SelectField for selecting the desired type of structure.
        english, french, german, spanish: SelectFields for language selection.
        submit: SubmitField for initiating the search.
    """
    typology = SelectField('🏠 Desired type of structure:')
    english = SelectField('🇬🇧 English language:',
                          choices=[('Vero', 'Yes'), ('Falso', 'No')])
    french = SelectField('🇫🇷 French language:',
                         choices=[('Vero', 'Yes'), ('Falso', 'No')])
    german = SelectField('🇩🇪 German language:',
                         choices=[('Vero', 'Yes'), ('Falso', 'No')])
    spanish = SelectField('🇪🇸 Spanish language:',
                          choices=[('Vero', 'Yes'), ('Falso', 'No')])
    submit = SubmitField('Search')


class SearchForm(FlaskForm):
    """
    Form class for searching luxurious structures.

    Attributes:
        indoor_pool: SelectField for indoor pool availability.
        sauna: SelectField for sauna availability.
        fitness_area: SelectField for fitness area availability.
        submit: SubmitField for initiating the search.
    """
    indoor_pool = SelectField('Indoor Pool:',
                              choices=[('Vero', 'Yes'), ('Falso', 'No')])
    sauna = SelectField('Sauna:',
                        choices=[('Vero', 'Yes'), ('Falso', 'No')])
    fitness_area = SelectField('Fitness area:',
                               choices=[('Vero', 'Yes'), ('Falso', 'No')])
    submit = SubmitField('Search')


class SearchTransport(FlaskForm):
    """
    Form class for searching hotels near transportation facilities.

    Attributes:
        selected_typology: SelectField for choosing typology.
        train_station: SelectField for choosing a train station.
        highway: SelectField for choosing a highway.
        submit: SubmitField for initiating the search.
    """
    selected_typology = SelectField('🏠 Typology:')
    train_station = SelectField('🚅 Train station:',
                                choices=[('Vero', 'Yes'), ('Falso', 'No')])
    highway = SelectField('🛣 Highway:',
                          choices=[('Vero', 'Yes'), ('Falso', 'No')])
    submit = SubmitField('Search')


class SearchExtras(FlaskForm):
    """
    Form class for searching structures with additional features.

    Attributes:
        air_conditioning: SelectField for Air Conditioning input.
        pets_allowed: SelectField for Pets Allowed input.
        submit: SubmitField for initiating the search.
    """
    air_conditioning_choices = [('Vero', 'Yes'), ('Falso', 'No')]
    pets_allowed_choices = [('Vero', 'Yes'), ('Falso', 'No')]
    air_conditioning = SelectField('Air Conditioning:',
                                   choices=air_conditioning_choices)
    pets_allowed = SelectField('Pets Allowed:',
                               choices=pets_allowed_choices)
    submit = SubmitField('Extras')


@app.route('/languages', methods=['GET', 'POST'])
def search_structures_periphery():
    """
    Route for searching structures in the periphery.

    Returns:
        str: Rendered HTML content for the peripherical B&B page.
    """
    form = SearchPeriphery()
    error_message = None

    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_typology')
    aux = json.loads(response.json())
    form.typology.choices = list(aux.values())

    if form.validate_on_submit():
        typology = form.typology.data
        english = form.english.data
        french = form.french.data
        german = form.german.data
        spanish = form.spanish.data

        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/find_structures_suburb?'
            f'Typology={typology}&'
            f'English={english}&'
            f'French={french}&'
            f'German={german}&'
            f'Spanish={spanish}'
        )

        try:
            response = requests.get(fastapi_url)
            response.raise_for_status()
            data_from_fastapi, error_message = response.json(), None
        except requests.exceptions.RequestException as e:
            data_from_fastapi, error_message = None, f'Error: {str(e)}'

        return render_template("languages.html", form=form,
                               result=data_from_fastapi,
                               error_message=error_message)

    return render_template('languages.html', form=form,
                           result=None, error_message=error_message)


@app.route('/luxuries', methods=['GET', 'POST'])
def search_structure_search():
    """
    Route for searching luxurious structures.

    Returns:
        str: Rendered HTML content for the wellness exploratory page.
    """
    form = SearchForm()
    error_message = None

    if form.validate_on_submit():
        sauna = form.sauna.data
        indoor_pool = form.indoor_pool.data
        fitness_area = form.fitness_area.data

        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/search_structures?'
            f'indoor_pool={indoor_pool}&'
            f'sauna={sauna}&'
            f'fitness_area={fitness_area}'
        )

        try:
            response = requests.get(fastapi_url)
            response.raise_for_status()
            data_from_fastapi, error_message = response.json(), None
        except requests.exceptions.RequestException as e:
            data_from_fastapi, error_message = None, f'Error: {str(e)}'

        return render_template("luxuries.html", form=form,
                               result=data_from_fastapi,
                               error_message=error_message)

    return render_template('luxuries.html', form=form,
                           result=None, error_message=error_message)


<<<<<<< Updated upstream
# Define a route for the Animal Crossers page
@app.route('/')
=======
@app.route('/index')
>>>>>>> Stashed changes
def index():
    """
    Route for displaying the homepage.

    Returns:
        str: Rendered HTML content for the homepage.
    """
    return render_template('index.html')


@app.route('/extras', methods=['GET', 'POST'])
def search_structure_periphery():
    """
    Route for searching structures with additional features.

    Returns:
        str: Rendered HTML content for the extras page.
    """
    form = SearchExtras(request.form)
    error_message = None
    result = None

    if form.validate_on_submit():
        air_conditioning = form.air_conditioning.data
        pets_allowed = form.pets_allowed.data

        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/essential_services_periphery?'
            f'air_conditioning={air_conditioning}&'
            f'pets_allowed={pets_allowed}'
        )

        try:
            response = requests.get(fastapi_url)

            if response.status_code == 200:
                result = response.json()
                return render_template('extras.html', form=form,
                                       result=result,
                                       error_message=error_message)
            else:
                error_message = 'Error fetching data from backend'

        except requests.RequestException as e:
            error_message = f'Error: {e}'

    return render_template('extras.html', form=form,
                           result=None, error_message=error_message)


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


@app.route('/transports', methods=['GET', 'POST'])
def find_hotels():
    """
    Route for searching hotels near transportation facilities.

    Returns:
        str: Rendered HTML content for the transports exploratory page.
    """
    form = SearchTransport()
    error_message = None
    data_from_fastapi = None

    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_typology')
    aux = json.loads(response.json())
    form.selected_typology.choices = list(aux.values())

    if form.validate_on_submit():
        selected_typology = form.selected_typology.data
        train_station = form.train_station.data
        highway = form.highway.data

        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/find_hotels_near_transports?'
            f'selected_typology={selected_typology}&'
            f'train_station={train_station}&'
            f'highway={highway}'
        )

        try:
            response = requests.get(fastapi_url)
            response.raise_for_status()
            data_from_fastapi = response.json()
        except requests.exceptions.RequestException as e:
            error_message = f'Error: {str(e)}'

    return render_template('transports.html', form=form,
                           result=data_from_fastapi,
                           error_message=error_message)


@app.route('/essentials', methods=['GET', 'POST'])
def find():
    """
    Route for searching essential services.

    Returns:
        str: Rendered HTML content for the essentials page.
    """
    form = SearchEssentials()
    error_message = None

    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_zones')
    aux = json.loads(response.json())
    form.zone.choices = list(aux.values())

    if form.validate_on_submit():
        zone = form.zone.data
        restaurant = form.restaurant.data
        parking = form.parking.data

        fastapi_url = (
            f'{FASTAPI_BACKEND_HOST}/structures?'
            f'zone={zone}&restaurant={restaurant}&parking={parking}'
        )

        try:
            response = requests.get(fastapi_url)
            response.raise_for_status()
            data_from_fastapi, error_message = response.json(), None
        except requests.exceptions.RequestException as e:
            data_from_fastapi, error_message = None, f'Error: {str(e)}'

        return render_template("essentials.html", form=form,
                               result=data_from_fastapi,
                               error_message=error_message)

    return render_template('essentials.html', form=form,
                           result=None, error_message=error_message)


@app.route('/home_page')
def home():
    """
    Route for displaying the explanatory homepage.

    Returns:
        str: Rendered HTML content for the homepage.
    """
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
