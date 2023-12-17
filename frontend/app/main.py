"""
Frontend module for the Flask application.
"""

from flask import Flask, render_template, request
import requests
from wtforms import StringField, SubmitField, SelectField
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

FASTAPI_BACKEND_HOST = 'http://backend'
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class SearchForm(FlaskForm):
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

    submit = SubmitField('Search')


@app.route('/search', methods=['GET', 'POST'])
def search_structure():
    """
    Route for handling search functionality.

    Returns:
        str: Rendered HTML content for the search page.
    """
    form = SearchForm(request.form)
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
                    'search.html',
                    form=form,
                    result=result,
                    error_message=error_message)
            else:
                error_message = 'Error fetching data from backend'

        except requests.RequestException as e:
            error_message = f'Error: {e}'

    return render_template(
        'search.html',
        form=form,
        result=None,
        error_message=error_message)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
