from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import json

app = FastAPI()

# Reading the CSV file
df = pd.read_csv('/app/app/dove-alloggiare.csv')

# Handling NA values
df.fillna('', inplace=True)


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
