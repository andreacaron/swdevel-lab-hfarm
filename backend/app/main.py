# Import FastAPI framework for building APIs quickly
from fastapi import FastAPI
# Import JSONResponse for returning custom JSON responses
from fastapi.responses import JSONResponse
# Import pandas for data manipulation and analysis
import pandas as pd
from fastapi.responses import JSONResponse
from datetime import datetime
from pydantic import BaseModel 
from flask import Flask, request, jsonify
import uvicorn



# Create an instance of the FastAPI application
app = FastAPI()

# Create a DataFrame
df = pd.read_csv('/app/app/dove-alloggiare.csv')
# Convert specific fields to strings and handle missing values
df["CAP"] = df["CAP"].astype(str)
df["CODICE IDENTIFICATIVO"] = df["CODICE IDENTIFICATIVO"].astype(str)
df.fillna('', inplace=True)

@app.get('/cerca_strutture')
def cerca_strutture(piscina_coperta,sauna,area_fitness):
    # Apply filters based on specified criteria
    filtro = (df['PISCINA COPERTA'] == piscina_coperta) & \
        (df['SAUNA'] == sauna) & \
        (df['FITNESS'] == area_fitness) & \
        (df['ZONA FIERA'] == 'Vero')
    # Extract filtered results as a dictionary of records
    risultato_filtrato = df[filtro].to_dict(orient='records')
    # Return the filtered results
    return risultato_filtrato


# Read CSV data into a pandas DataFrame
df_suburb = pd.read_csv('/app/app/dove-alloggiare.csv')

''' Handle missing values (NA) by replacing them
with empty strings in the DataFrame '''
df_suburb.fillna('', inplace=True)


@app.get("/find_structures_suburb")
# Extract relevant data for the frontend based on specified conditions
def find_structures_suburb(Typology, English, French, German, Spanish):
    conditions = (
        (df_suburb['TIPOLOGIA'] == Typology) &
        (df_suburb['INGLESE'] == English) &
        (df_suburb['FRANCESE'] == French) &
        (df_suburb['TEDESCO'] == German) &
        (df_suburb['SPAGNOLO'] == Spanish) &
        (df_suburb['PERIFERIA'] == 'Vero')
    )
# Filter DataFrame based on conditions and convert
# the results to a list of dictionaries
    results = df_suburb[conditions].to_dict(orient='records')
    return results

@app.get("/get_typology")
def get_typology():
    #  Extract unique values of 'TIPOLOGIA' column from DataFrame
    df_tipologie = df_suburb['TIPOLOGIA'].drop_duplicates()
    # Convert the unique values to JSON format
    return df_tipologie.to_json()

