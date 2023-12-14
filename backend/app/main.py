from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import uvicorn

app = FastAPI()

df_suburb = pd.read_csv('/app/app/dove-alloggiare.csv')

# Handling NA values
df_suburb.fillna('', inplace=True)

@app.get("/find_structures_suburb")
def find_structures_suburb(Typology,English,French,German,Spanish):

    # Extract relevant data for the frontend
    conditions = (df_suburb['TIPOLOGIA'] == Typology) & \
        (df_suburb['INGLESE'] == English) & \
        (df_suburb['FRANCESE'] == French) & \
        (df_suburb['TEDESCO'] == German) & \
        (df_suburb['SPAGNOLO'] == Spanish)& \
        (df_suburb['PERIFERIA'] == 'Vero')
    
    results = df_suburb[conditions].to_dict(orient='records')
    return results

@app.get("/get_typology")
def get_typology():
    df_tipologie = df_suburb['TIPOLOGIA'].drop_duplicates()
    return df_tipologie.to_json()

if __name__ == "__main__":
    # Start server FastAPI
    uvicorn.run(app, host="127.0.0.1", port=8081)

#/find_structures_suburb?Typology=ALBERGO&English=Vero&French=Vero&German=Vero&Spanish=Vero
