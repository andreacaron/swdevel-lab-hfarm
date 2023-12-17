<<<<<<< HEAD
# FastAPI imports
from fastapi import FastAPI, Query
=======
"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
>>>>>>> Feature_2
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Pandas and datetime imports
import pandas as pd
<<<<<<< HEAD
from datetime import datetime

# Pydantic import
from pydantic import BaseModel

# Flask and related imports
from flask import Flask, request, jsonify
from flask_cors import CORS

# Uvicorn import
import uvicorn

=======
import app
from pydantic import BaseModel
>>>>>>> Feature_2

# Create an instance of the FastAPI application
app = FastAPI()
<<<<<<< HEAD

# Adding CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Function to parse string values to boolean ('True'/'False'/'Vero'/'Falso')
def parse_bool(value):
    """
    Parses string values to boolean.

    Args:
        value (str): The string value to be parsed.

    Returns:
        bool: Boolean value of the input string.
    """
    return value.lower() in ['true', 'vero']

=======
>>>>>>> Feature_2
# Create a DataFrame
df = pd.read_csv('/app/app/dove-alloggiare.csv')
# Convert specific fields to strings and handle missing values
df["CAP"] = df["CAP"].astype(str)
df["CODICE IDENTIFICATIVO"] = df["CODICE IDENTIFICATIVO"].astype(str)
df.fillna('', inplace=True)


@app.get('/cerca_strutture')
def cerca_strutture(piscina_coperta, sauna, area_fitness):
    # Apply filters based on specified criteria
    filtro = (
        (df['PISCINA COPERTA'] == piscina_coperta) &
        (df['SAUNA'] == sauna) &
        (df['FITNESS'] == area_fitness) &
        (df['ZONA FIERA'] == 'Vero')
    )

    # Extract filtered results as a dictionary of records
    risultato_filtrato = df[filtro].to_dict(orient='records')
    # Return the filtered results
    return risultato_filtrato


<<<<<<< HEAD
# Read CSV data into a pandas DataFrame
df_suburb = pd.read_csv('/app/app/dove-alloggiare.csv')
'''
Handle missing values (NA) by replacing them
with empty strings in the DataFrame 
'''
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


# Function to read and filter B&B based on user-selected amenities
@app.get("/essential_services_periphery")
def essential_services_periphery(
    aria_condizionata: str = Query("False", description="Air Conditioning"),
    animali_ammessi: str = Query("False", description="Pets Allowed")
):
    """
    Retrieves B&B data based on selected amenities in periphery areas.

    Args:
        aria_condizionata (str): indicating Air Conditioning preference.
        animali_ammessi (str): indicating Pets Allowed preference.

    Returns:
        List[Dict[str, str]]: Filtered B&B data with relevant information.
    """

    # Parsing amenities to boolean values
    aria_condizionata_bool = parse_bool(aria_condizionata)
    animali_ammessi_bool = parse_bool(animali_ammessi)

    # Reading the CSV file containing bed and breakfast data
    df = pd.read_csv('app/dove-alloggiare.csv')

    # Handling NA values
    df.fillna('', inplace=True)

    # Filter bed and breakfast from 'TIPOLOGIA' column
    bnb_df = df[df['TIPOLOGIA'] == 'BED AND BREAKFAST']

    # Filter B&B in periphery areas
    periphery_bnb = bnb_df[bnb_df['PERIFERIA'] == 'Vero']

    # Filtering essential services for B&B based on user-selected amenities
    filter_conditions = (
        (periphery_bnb['ARIA CONDIZIONATA'] == aria_condizionata) &
        (periphery_bnb['ANIMALI AMMESSI'] == animali_ammessi)
    )

    essential_df = periphery_bnb[filter_conditions]

    # Extract relevant data for frontend
    essential_data = essential_df[
        [
            'DENOMINAZIONE',
            'INDIRIZZO',
            'NUMERO CIVICO',
            'COMUNE',
            'CAP',
            'PROVINCIA',
            'TELEFONO',
            'EMAIL'
        ]
        ].to_dict(orient='records')

    return essential_data
=======
@app.get('/find_hotels_near_transports')
def find_hotels_near_transports(selected_typology, stazione, autostrada):
    # Filtering data based on the criteria
    filter = (
        (df['TIPOLOGIA'] == selected_typology) &
        (df['STAZIONE FS'] == stazione) &
        (df['AUTOSTRADA'] == autostrada)
        )
    filtered_result = df[filter].to_dict(orient='records')
    return filtered_result


@app.get("/get_typology")
def get_typology():
    df_tipologie = df['TIPOLOGIA'].drop_duplicates()
    return df_tipologie.to_json()
>>>>>>> Feature_2


# Extracting relevant data for zona, parking and restaurant for the frontend
@app.get("/structures")
def structures(zona, parcheggio, ristorante):
    filter = (df['ZONA '] == zona) & \
             (df['RISTORANTE'] == ristorante) & \
             (df['PARCHEGGIO'] == parcheggio)
    final_result = df[filter].to_dict(orient='records')

    return final_result


# Getting unique zones for the frontend
@app.get("/get_zones")
def get_zones():
    zones_df = df['ZONA '].drop_duplicates()
    return zones_df.to_json()