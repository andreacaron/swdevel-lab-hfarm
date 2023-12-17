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
from wtforms import StringField, SubmitField, SelectField, SelectFieldte

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  # Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class QueryForm(FlaskForm):
    person_name = StringField('Person Name:')
    submit = SubmitField('Get Birthday from FastAPI Backend')


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
    backend_url = 'http://backend/get-date'  # Adjust the URL based on your backend configuration
    try:
        response = requests.get(backend_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get('date', 'Date not available')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching date from backend: {e}")
        return 'Date not available'


@app.route('/internal', methods=['GET', 'POST'])
def internal():
    """
    Render the internal page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    form = QueryForm()
    error_message = None  # Initialize error message

    if form.validate_on_submit():
        person_name = form.person_name.data

        # Make a GET request to the FastAPI backend
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/query/{person_name}'
        response = requests.get(fastapi_url)

        if response.status_code == 200:
            # Extract and display the result from the FastAPI backend
            data = response.json()
            result = data.get('birthday', f'Error: Birthday not available for {person_name}')
            return render_template('internal.html', form=form, result=result, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch birthday for {person_name} from FastAPI Backend'

    return render_template('internal.html', form=form, result=None, error_message=error_message)


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
