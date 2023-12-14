"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
from pydantic import BaseModel 
from flask import Flask, request, jsonify 



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




