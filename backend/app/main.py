from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

@app.get('/find_structure')
def find_structure(selected_type: str):
    # Read the CSV file
    df_structures = pd.read_csv('app/dove-alloggiare.csv')
   
    # Handling NA values
    df_structures.fillna('', inplace=True)


    # Filtering the data based on the criteria of the present feature
    conditions = df_structures[(df_structures['TIPOLOGIA'] == selected_type) &  
                (df_structures['PERIFERIA'] == 'Vero') &
                (df_structures['INGLESE'] == 'Vero') &
                (df_structures['SPAGNOLO'] == 'Vero')]
   
    # If there is data in the specified typology, return the structures' name, address, and email
    results = conditions[['DENOMINAZIONE', 'PROVINCIA', 'COMUNE', 'INDIRIZZO', 'EMAIL']].to_dict(orient='records')
       
    return results


if __name__ == "__main__":
    # Start server FastAPI
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)


