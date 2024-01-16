"""
Backend module for a FastAPI application providing
accommodation and facility search functionality.

This module defines a FastAPI application
that serves as the backend for the project.
"""

# Import FastAPI and related modules
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Import Pandas for data manipulation
import pandas as pd

# Import Pydantic for data validation
from pydantic import BaseModel

# Import the app module
import app

# Create an instance of the FastAPI application
app = FastAPI()

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


# Create a DataFrame
df = pd.read_csv('/app/app/dove-alloggiare.csv')

# Handle missing values (NA) by replacing them
df.fillna('', inplace=True)

# Convert specific fields to strings and handle missing values
df["CAP"] = df["CAP"].astype(str)
df["CODICE IDENTIFICATIVO"] = df["CODICE IDENTIFICATIVO"].astype(str)
df.fillna('', inplace=True)


# Endpoint to search for structures based on specified criteria:
@app.get('/search_structures')
def search_structures(indoor_pool, sauna, fitness_area):
    """
    Endpoint to search for structures based on specified criteria.

    Args:
        indoor_pool (str): Indicates the preference for a covered pool.
        sauna (str): Indicates the preference for a sauna.
        fitness_area (str): Indicates the preference for a fitness area.

    Returns:
        List[Dict[str, Any]]: Filtered results of structures as a list of
        dictionaries.
    """
    # Apply filters based on specified criteria
    filter = (
        (df['PISCINA COPERTA'] == indoor_pool) &
        (df['SAUNA'] == sauna) &
        (df['FITNESS'] == fitness_area) &
        (df['ZONA FIERA'] == 'Vero')
    )

    # Extract filtered results as a dictionary of records
    filtered_result = df[filter].to_dict(orient='records')
    # Return the filtered results
    return filtered_result


# Endpoint to search for suburbs based on specified criteria
@app.get("/find_structures_suburb")
# Extract relevant data for the frontend based on specified conditions
def find_structures_suburb(Typology, English, French, German, Spanish):
    """
    Endpoint to search for suburbs based on specified criteria.

    Args:
        Typology (str): The type of structure.
        English (str): Indicates English language availability.
        French (str): Indicates French language availability.
        German (str): Indicates German language availability.
        Spanish (str): Indicates Spanish language availability.

    Returns:
        List[Dict[str, Any]]: Filtered results of suburbs as a list
        of dictionaries.
    """
    conditions = (
        (df['TIPOLOGIA'] == Typology) &
        (df['INGLESE'] == English) &
        (df['FRANCESE'] == French) &
        (df['TEDESCO'] == German) &
        (df['SPAGNOLO'] == Spanish) &
        (df['PERIFERIA'] == 'Vero')
    )
    # Filter DataFrame based on conditions and convert
    # the results to a list of dictionaries
    results = df[conditions].to_dict(orient='records')
    return results


# Endpoint to search for structures typologies
@app.get("/get_typology")
def get_typology():
    """
    Endpoint to retrieve unique structure typologies.

    Returns:
        str: Unique structure typologies in JSON format.
    """
    # Extract unique values of 'TIPOLOGIA' column from DataFrame
    df_typologies = df['TIPOLOGIA'].drop_duplicates()
    # Convert the unique values to JSON format
    return df_typologies.to_json()


# Function to read and filter B&B based on user-selected amenities
@app.get("/essential_services_periphery")
def essential_services_periphery(
    air_conditioning: str = Query("False", description="Air Conditioning"),
    pets_allowed: str = Query("False", description="Pets Allowed")
):
    """
    Retrieves B&B data based on selected amenities in periphery areas.

    Args:
        air_conditioning (str): Indicates Air Conditioning preference.
        pets_allowed (str): Indicates Pets Allowed preference.

    Returns:
        List[Dict[str, str]]: Filtered B&B data with relevant information.
    """
    # Parsing amenities to boolean values
    air_conditioning_bool = parse_bool(air_conditioning)
    pets_allowed_bool = parse_bool(pets_allowed)

    # Filter bed and breakfast from 'TIPOLOGIA' column
    bnb_df = df[df['TIPOLOGIA'] == 'BED AND BREAKFAST']

    # Filter B&B in periphery areas
    periphery_bnb = bnb_df[bnb_df['PERIFERIA'] == 'Vero']

    # Filtering essential services for B&B based on user-selected amenities
    filter_conditions = (
        (periphery_bnb['ARIA CONDIZIONATA'] == air_conditioning) &
        (periphery_bnb['ANIMALI AMMESSI'] == pets_allowed)
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


# Endpoint to search for typology structures based on specified criteria
@app.get('/find_hotels_near_transports')
def find_hotels_near_transports(
    selected_typology,
    train_station,
    highway
):

    """
    Endpoint to search for hotels near transportation based
    on specified criteria.

    Args:
        selected_typology (str): The selected structure typology.
        train_station (str): The selected train station.
        highway (str): The selected highway.

    Returns:
        List[Dict[str, Any]]: Filtered results of hotels
        near transportation as a list of dictionaries.
    """
    # Filtering data based on the criteria
    filter_transports = (df['TIPOLOGIA'] == selected_typology) & \
        (df['STAZIONE FS'] == train_station) & \
        (df['AUTOSTRADA'] == highway)
    filtered_result = df[filter_transports].to_dict(orient='records')
    return filtered_result


# Extracting relevant data for zona, parking, and restaurant for the frontend
@app.get("/structures")
def structures(zone, parking, restaurant):
    """
    Endpoint to extract relevant data for the frontend
    based on specified criteria.

    Args:
        zone (str): The selected zone.
        parking (str): The selected parking preference.
        restaurant (str): The selected restaurant preference.

    Returns:
        List[Dict[str, Any]]: Filtered results of relevant
        data as a list of dictionaries.
    """
    filter_conditions = (df['ZONA '] == zone) & \
        (df['RISTORANTE'] == restaurant) & \
        (df['PARCHEGGIO'] == parking)
    final_result = df[filter_conditions].to_dict(orient='records')

    return final_result


# Getting unique zones for the frontend
@app.get("/get_zones")
def get_zones():
    """
    Endpoint to retrieve unique zones for the frontend.

    Returns:
        str: Unique zones in JSON format.
    """
    zones_df = df['ZONA '].drop_duplicates()
    return zones_df.to_json()
