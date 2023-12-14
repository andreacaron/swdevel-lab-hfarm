"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template
import requests 
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

class SearchForm(FlaskForm):
    typology = SelectField('Desired type of structure:')
    english = SelectField('English language:', choices=[('Vero', 'Si'), ('Falso', 'No')])
    french = SelectField('French language:', choices=[('Vero', 'Si'), ('Falso', 'No')])
    german = SelectField('German language:', choices=[('Vero', 'Si'), ('Falso', 'No')])
    spanish = SelectField('Spanish language:', choices=[('Vero', 'Si'), ('Falso', 'No')])
    
    submit = SubmitField('Search')

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'

@app.route('/periferia', methods=['GET', 'POST'])
def search_structure():
    form = SearchForm()
    error_message = None

    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_typology')
    aux = json.loads(response.json())
    form.typology.choices = list(aux.values())

    if form.validate_on_submit():
        type_structure = form.typology.data
        english = form.english.data
        french = form.french.data
        german = form.german.data
        spanish = form.spanish.data
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/find_structures_suburb?Typology={type_structure}&English={english}&French={french}&German={german}&Spanish={spanish}'
        try:
            response = requests.get(fastapi_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data_from_fastapi, error_message = response.json(), None
        except requests.exceptions.RequestException as e:
            data_from_fastapi, error_message = None, f'Error: {str(e)}'

        return render_template("periferia.html", form=form, result=data_from_fastapi, error_message=error_message)

    return render_template('periferia.html', form=form, result=None, error_message=error_message)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
