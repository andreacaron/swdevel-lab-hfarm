# Importing necessary modules
from flask import Flask, render_template, request
import requests
from wtforms import StringField, SubmitField, SelectField
from flask_wtf import FlaskForm
import pandas as pd

# Creating a Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' # Setting the secret key for CSRF protection

# Defining the FastAPI backend host
FASTAPI_BACKEND_HOST = 'http://backend'
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'

# Defining the search form using Flask-WTF
class SearchForm(FlaskForm):
    # Create SelectFields for user input
    aria_condizionata = SelectField('Air Conditioning:', choices=[('Vero', 'Yes'), ('Falso', 'No')])
    animali_ammessi = SelectField('Pets Allowed:', choices=[('Vero', 'Yes'), ('Falso', 'No')])
    submit = SubmitField('Search')

# Defining the route for search functionality
@app.route('/search', methods=['GET', 'POST'])
def search_structure():
    # Create a form instance
    form = SearchForm(request.form)
    error_message = None
    result = None

    # Handling form submission
    if form.validate_on_submit():
        aria_condizionata = form.aria_condizionata.data
        animali_ammessi = form.animali_ammessi.data

        # Making a request to the FastAPI backend with user input
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/essential_services_periphery?aria_condizionata={aria_condizionata}&animali_ammessi={animali_ammessi}'
        
        # Requesting data from the FastAPI backend
        response = requests.get(fastapi_url)

        # Process response from the FastAPI backend
        if response.status_code == 200:
             # Extracting and displaying the result from the FastAPI backend
            data = response.json()
            result = data  # Assigning the retrieved data to 'result'
            return render_template('search.html', form=form, result=result, error_message=error_message)
        else:
            error_message = f'Error'

    # Rendering the search.html template with form and error_message
    return render_template('search.html', form=form, result=None, error_message=error_message)

# Defining another route to display mock search results
@app.route('/display_results', methods=['GET'])
def display_results():
    # Mock search results data (can be replaced with real data)
    result = [
        {
            'DENOMINAZIONE': 'Hotel 1',
            'PROVINCIA': 'Province 1',
            'COMUNE': 'City 1',
            'INDIRIZZO': 'Address 1',
            'NUMERO CIVICO': '123',
            'CAP': '12345',
            'EMAIL': 'hotel1@example.com'
        },
    ]

    # Rendering the results.html template with result data
    return render_template('results.html', result=result)  

# Starting the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)