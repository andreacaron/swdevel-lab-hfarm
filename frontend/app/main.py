# Importing the necessary libraries
import requests  
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms import StringField, SubmitField
import json
from flask import Flask, render_template
import requests

# Creating an instance of the Flask class
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  

# Defining a FlaskForm for the search input fields
class SearchForm(FlaskForm):
   zona = SelectField('Zone:')
   ristorante = SelectField('Restaurant:', choices=[('Vero', 'Yes'), ('Falso', 'No')])
   parcheggio = SelectField('Parking', choices=[('Vero', 'Yes'), ('Falso', 'NO')])
   submit = SubmitField('Search')

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'

# Defining a route for the internal page
@app.route('/internal_page', methods=['GET', 'POST'])
def find():
   form = SearchForm()
   error_message = None
   response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_zones')
   aux = json.loads(response.json())
   form.zona.choices = list(aux.values())

   if form.validate_on_submit():
       zona = form.zona.data
       ristorante = form.ristorante.data
       parcheggio = form.parcheggio.data
       fastapi_url = f'{FASTAPI_BACKEND_HOST}/structures?zona={zona}&ristorante={ristorante}&parcheggio={parcheggio}'
       try:
           response = requests.get(fastapi_url)
           response.raise_for_status()  # Raise an HTTPError for bad responses
           data_from_fastapi, error_message = response.json(), None
       except requests.exceptions.RequestException as e:
           data_from_fastapi, error_message = None, f'Error: {str(e)}'


       return render_template("internal_page.html", form=form, result=data_from_fastapi, error_message=error_message)

   return render_template('internal_page.html', form=form, result=None, error_message=error_message)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)

