import os
import sys
from fastapi.testclient import TestClient

# Setting the path for importing the FastAPI application
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

# Creating a test client to interact with the FastAPI app
client = TestClient(app)

# Testing case: Filter with invalid input for 'aria_condizionata' and valid 'animali_ammessi'
def test_invalid_input():
    response = client.get("/essential_services_periphery?aria_condizionata=Invalid&animali_ammessi=True")
    assert response.status_code == 200 

# Testing case: No query parameters provided
def test_no_query_params():
    response = client.get("/essential_services_periphery")
    assert response.status_code == 200
    
# Testing case: Accessing an invalid endpoint
def test_invalid_endpoint():
    response = client.get("/essential_services_periphery_invalid")
    assert response.status_code == 404

# Testing case: No query parameters provided
def test_all_false():
    response = client.get("/essential_services_periphery")
    assert response.status_code == 200  
    assert response.json() == []  # Ensuring the response JSON is an empty list

# Testing case: Filter with 'aria_condizionata' set to True
def test_air_conditioning_true():
    response = client.get("/essential_services_periphery?aria_condizionata=True")
    assert response.status_code == 200  

# Testing case: Filter with 'animali_ammessi' set to True
def test_pets_allowed_true():
    response = client.get("/essential_services_periphery?animali_ammessi=True")
    assert response.status_code == 200 

# Testing case: Filter with both 'aria_condizionata' and 'animali_ammessi' set to True
def test_both_true():
    response = client.get("/essential_services_periphery?aria_condizionata=True&animali_ammessi=True")
    assert response.status_code == 200  

# Testing case: Filter with both 'aria_condizionata' and 'animali_ammessi' set to False
def test_both_false():
    response = client.get("/essential_services_periphery?aria_condizionata=False&animali_ammessi=False")
    assert response.status_code == 200  
    assert response.json() == []  

# Testing case: Filter with 'aria_condizionata' set to True and 'animali_ammessi' set to False
def test_air_conditioning_true_pets_false():
    response = client.get("/essential_services_periphery?aria_condizionata=True&animali_ammessi=False")
    assert response.status_code == 200  

# Testing case: Filter with 'aria_condizionata' set to False and 'animali_ammessi' set to True
def test_air_conditioning_false_pets_true():
    response = client.get("/essential_services_periphery?aria_condizionata=False&animali_ammessi=True")
    assert response.status_code == 200  

# Testing case: Filter with 'aria_condizionata' set to an invalid input
def test_invalid_air_conditioning_param():
    response = client.get("/essential_services_periphery?aria_condizionata=123")
    assert response.status_code == 200  

# Testing case: Filter with 'animali_ammessi' set to an invalid input
def test_invalid_pets_allowed_param():
    response = client.get("/essential_services_periphery?animali_ammessi=Random")
    assert response.status_code == 200  

# Testing case: Filter with both 'aria_condizionata' and 'animali_ammessi' set to invalid inputs
def test_combination_invalid_params():
    response = client.get("/essential_services_periphery?aria_condizionata=Invalid&animali_ammessi=Random")
    assert response.status_code == 200  

# Testing case: Filter with 'aria_condizionata' set to a valid input and 'animali_ammessi' set to an invalid input
def test_combination_valid_and_invalid_params():
    response = client.get("/essential_services_periphery?aria_condizionata=True&animali_ammessi=Random")
    assert response.status_code == 200  

# Testing case: Filter with 'aria_condizionata' set to a large string input
def test_large_query_params():
    long_string = "a" * 10000  # Creating a long query parameter value
    response = client.get(f"/essential_services_periphery?aria_condizionata={long_string}")
    assert response.status_code == 200  

# Testing case: for invalid air conditioning parameter and no pets allowed
def test_invalid_air_conditioning_param_and_no_pets_allowed():
    response = client.get("/essential_services_periphery?aria_condizionata=123&animali_ammessi=False")
    assert response.status_code == 200  

# Testing case: for valid air conditioning parameter and invalid pets allowed
def test_valid_air_conditioning_param_and_invalid_pets_allowed():
    response = client.get("/essential_services_periphery?aria_condizionata=True&animali_ammessi=Invalid")
    assert response.status_code == 200  

# Testing case: for no air conditioning parameter and valid pets allowed
def test_no_air_conditioning_param_and_valid_pets_allowed():
    response = client.get("/essential_services_periphery?animali_ammessi=True")
    assert response.status_code == 200  

# Testing case: for no pets allowed parameter and valid air conditioning
def test_no_pets_allowed_param_and_valid_air_conditioning():
    response = client.get("/essential_services_periphery?aria_condizionata=True")
    assert response.status_code == 200  

# Testing case: with large query parameter for pets allowed set to True
def test_large_query_params_pets_allowed_true():
    long_string = "a" * 10000
    response = client.get(f"/essential_services_periphery?animali_ammessi=True&aria_condizionata={long_string}")
    assert response.status_code == 200

# Testing case: Filter with 'aria_condizionata' set to False and 'animali_ammessi' set to True
def test_air_conditioning_false_pets_true():
    response = client.get("/essential_services_periphery?aria_condizionata=False&animali_ammessi=True")
    assert response.status_code == 200  

# Testing case: Filter with both 'aria_condizionata' and 'animali_ammessi' set to True
def test_both_true_pets_false():
    response = client.get("/essential_services_periphery?aria_condizionata=True&animali_ammessi=False")
    assert response.status_code == 200  

# Testing case: Filter with 'aria_condizionata' set to False and 'animali_ammessi' set to False
def test_both_false_pets_true():
    response = client.get("/essential_services_periphery?aria_condizionata=False&animali_ammessi=True")
    assert response.status_code == 200  

# Testing case: Filter with 'aria_condizionata' set to True and 'animali_ammessi' set to True
def test_both_true_pets_true():
    response = client.get("/essential_services_periphery?aria_condizionata=True&animali_ammessi=True")
    assert response.status_code == 200  


