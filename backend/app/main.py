"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
import app
from pydantic import BaseModel

app = FastAPI()
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
