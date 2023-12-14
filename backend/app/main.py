# This script sets up a FastAPI server to filter bed and breakfast establishments based on selected amenities.
# It utilizes CORS middleware for cross-origin requests.

# Importing necessary modules
import csv
from fastapi import FastAPI, Query
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Code to create an instance of FastAPI
app = FastAPI()

# Adding CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Setting '*' to allow requests from any origin 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# Function to parse string values to boolean ('True'/'False'/'Vero'/'Falso')
def parse_bool(value):
    return value.lower() in ['true', 'vero']


# Function to read and filter B&B based on user-selected amenities
@app.get("/essential_services_periphery")
def essential_services_periphery(aria_condizionata: str = Query("False", description="Air Conditioning"),
                                 animali_ammessi: str = Query("False", description="Pets Allowed")):
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
    
    # Filtering essential services for B&B in periphery based on user-selected amenities
    filter_conditions = (periphery_bnb['ARIA CONDIZIONATA'] == aria_condizionata) & \
                         (periphery_bnb['ANIMALI AMMESSI'] == animali_ammessi)
    
    essential_df = periphery_bnb[filter_conditions]
    
    # Extract relevant data for frontend
    essential_data = essential_df[
        ['DENOMINAZIONE', 'INDIRIZZO', 'NUMERO CIVICO', 'COMUNE', 'CAP', 'PROVINCIA', 'EMAIL']
    ].to_dict(orient='records')

    return essential_data

