import os
import sys
from fastapi.testclient import TestClient
import unittest
import pandas as pd

# Add the parent directory to the sys.path
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from app.main import app, df_suburb
from app.main import find_structures_suburb
import pytest

# Create a TestClient instance for testing API endpoints
client = TestClient(app)


def test_suburb_albergo_lang():
    # Test Albergo all languages
    response = client.get("/find_structures_suburb", params={
        'Typology': 'ALBERGO',
        'English': 'True',
        'French': 'True',
        'German': 'True',
        'Spanish': 'True'
    })
    assert response.status_code == 200
    # Check if the reponse is a list
    assert isinstance(response.json(), list)


def test_suburb_albergo_nolang():
    # Test albergo no language
    response = client.get("/find_structures_suburb", params={
        'Typology': 'ALBERGO',
        'English': 'Falso',
        'French': 'Falso',
        'German': 'Falso',
        'Spanish': 'Falso'
    })
    # Check if the reponse is a list
    assert isinstance(response.json(), list)


def test_suburb_bed_and_breakfast():
    # Test Bed and breakfast all languages
    response = client.get("/find_structures_suburb", params={
        'Typology': 'BED AND BREAKFAST',
        'English': 'Vero',
        'French': 'Vero',
        'German': 'Vero',
        'Spanish': 'Vero'
    })
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    # Check if the response content is a list
    assert isinstance(response.json(), list)
    # Check if the response list has at least one item
    assert len(response.json()) > 0


def test_suburb_residence():
    # Test Residence all languages
    response = client.get("/find_structures_suburb", params={
        'Typology': 'RESIDENCE',
        'English': 'Vero',
        'French': 'Vero',
        'German': 'Vero',
        'Spanish': 'Vero'
    })
    # Check if the response content is a list
    assert isinstance(response.json(), list)
    # Check if the response list has at least one item
    assert len(response.json()) > 0


def test_suburb_invalid():
    # Test invalide typology
    response = client.get("/find_structures_suburb", params={
        'Typology': 'COUNTRYHOUSE',
        'English': 'Vero',
        'French': 'Vero',
        'German': 'Vero',
        'Spanish': 'Vero'
    })
    # Check if the response content is a list
    assert isinstance(response.json(), list)
    # Check if the response list is empty
    assert len(response.json()) == 0


def test_suburbs_hotel():
    # Test invalid typology
    response = client.get("/find_structures_suburb", params={
        'Typology': 'HOTEL',
        'English': 'Vero',
        'French': 'Vero',
        'German': 'Vero',
        'Spanish': 'Vero'
    })
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    # Check if the response content is an empty list
    assert response.json() == []


def test_suburb_missing_values():
    # Test to ensure no missing values
    assert not df_suburb.isna().any().any()


class TestSearchStructures(unittest.TestCase):

    def test_casa_vacanze(self):
        # Test casa vacanze no German
        # Call the find_structures_suburb function with specific parameters
        result = find_structures_suburb(
            Typology='CASA PER VACANZE',
            English='Vero',
            French='Vero',
            German='Falso',
            Spanish='Vero'
        )
        # Check if the result is a list
        self.assertIsInstance(result, list)

    def test_ostello(self):
        # Test ostello only English
        result = find_structures_suburb(
            Typology='OSTELLO',
            English='Vero',
            French='Falso',
            German='Falso',
            Spanish='Falso'
        )
        self.assertIsInstance(result, list)

    def test_bed_and_breakfast(self):
        # Test bed and breakfast only Spanish
        result = find_structures_suburb(
            Typology='BED AND BREAKFAST',
            English='Falso',
            French='Falso',
            German='Falso',
            Spanish='Vero'
        )
        self.assertIsInstance(result, list)

    def test_campeggio(self):
        # Test campeggio no language
        result = find_structures_suburb(
            Typology='CAMPEGGIO',
            English=False,
            French=False,
            German=False,
            Spanish=False
        )
        self.assertIsInstance(result, list)
        # Check if the result list is empty
        self.assertEqual(len(result), 0)

    def test_casa_religiosa(self):
        # Test casa religiosa di ospitalità no language
        result = find_structures_suburb(
            Typology="CASA RELIGIOSA DI OSPITALITA' ",
            English=False,
            French=False,
            German=False,
            Spanish=False
        )
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)
