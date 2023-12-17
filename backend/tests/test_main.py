import os
import sys
import unittest
import pytest
# Add the project root to the sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


# Test to check if the endpoint returns data for valid filters
# Assuming there is data for the specified filters
def test_get_structures_with_data():
    response = client.get(
        "/structures",
        params={
            'zona': 'dolomiti',
            'parcheggio': 'Vero',
            'ristorante': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


# Test to check if the endpoint handles no data for given filters
# Assuming no data matches the specified filters
def test_get_structures_no_data():
    response = client.get(
        "/structures",
        params={
            'zona': 'nonexistent',
            'parcheggio': 'Falso',
            'ristorante': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


# Test to check if the /get_zones endpoint returns non-empty data
def test_get_zones_not_empty():
    response = client.get("/get_zones")
    assert response.status_code == 200
    assert response.json()
    print("Response:", response.json())


# Test to check if the endpoint handles an invalid filter parameter
def test_invalid_filter_parameter():
    response = client.get(
        "/structures",
        params={
            'zone': 'australia',
            'ristorante': 'Vero',
            'parcheggio': 'Falso'
        }
    )
    assert response.status_code == 422  # Assuming 422 for bad request


# Test to check if the endpoint returns data for a specific zone (dolomiti)
def test_zone_dolomiti():
    response = client.get(
        "/structures",
        params={
            'zona': 'dolomiti',
            'parcheggio': 'Vero',
            'ristorante': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (caorle)
def test_zone_caorle():
    response = client.get(
        "/structures",
        params={'zona': 'caorle', 'parcheggio': 'Falso', 'ristorante': 'Vero'}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (jesolo-eraclea)
def test_zone_jesolo_eraclea():
    response = client.get(
        "/structures",
        params={
            'zona': 'jesolo-eraclea',
            'parcheggio': 'Vero',
            'ristorante': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (bibione)
def test_zone_bibione():
    response = client.get(
        "/structures",
        params={
            'zona': 'bibione',
            'parcheggio': 'Falso',
            'ristorante': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (altopiano-asiago)
def test_zone_altopiano_asiago():
    response = client.get(
        "/structures",
        params={
            'zona': 'altopiano-asiago',
            'parcheggio': 'Vero',
            'ristorante': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (belluno-feltre-alpago)
def test_zone_belluno_feltre_alpago():
    response = client.get(
        "/structures",
        params={
            'zona': 'belluno-feltre-alpago',
            'parcheggio': 'Falso',
            'ristorante': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (cavallino)
def test_zone_cavallino():
    response = client.get(
        "/structures",
        params={
            'zona': 'cavallino',
            'parcheggio': 'Vero',
            'ristorante': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (chioggia)
def test_zone_chioggia():
    response = client.get(
        "/structures",
        params={
            'zona': 'chioggia',
            'parcheggio': 'Falso',
            'ristorante': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (garda)
def test_zone_garda():
    response = client.get(
        "/structures",
        params={
            'zona': 'garda',
            'parcheggio': 'Falso',
            'ristorante': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (padova)
def test_zone_padova():
    response = client.get(
        "/structures",
        params={
            'zona': 'padova',
            'parcheggio': 'Vero',
            'ristorante': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (rovigo)
def test_zone_rovigo():
    response = client.get(
        "/structures",
        params={
            'zona': 'rovigo',
            'parcheggio': 'Falso',
            'ristorante': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (terme-euganee)
def test_zone_terme_euganee():
    response = client.get(
        "/structures",
        params={
            'zona': 'terme-euganee',
            'parcheggio': 'Vero',
            'ristorante': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (treviso)
def test_zone_treviso():
    response = client.get(
        "/structures",
        params={
            'zona': 'treviso',
            'parcheggio': 'Falso',
            'ristorante': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (venezia)
def test_zone_venezia():
    response = client.get(
        "/structures",
        params={
            'zona': 'venezia',
            'parcheggio': 'Vero',
            'ristorante': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/

"""