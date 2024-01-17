"""
Module for Backend Testing:

Objective:
- Validate the functionality of the backend code.

Expected Outcome:
- Efficient execution of tests means backend code functions as expected.

To execute tests by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
"""

# Importing all necessary libraries
import os
import sys
import pytest
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse
import pandas as pd
import unittest

# Skipping performance tests
pytest.mark.performance = pytest.mark.skip(reason="Performance tests skipped")

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

# Import statements
from app.main import app, search_structures, essential_services_periphery, df, find_structures_suburb

# Creating a test client to interact with the FastAPI app

client = TestClient(app)

class TestSearchStructures(unittest.TestCase):
    """
    Test cases for the search_structures endpoint.

    These tests cover various scenarios for searching
    structures based on specified criteria.
    """

    def setUp(self):
        self.client = TestClient(app)

    def test_search_with_all_options_true(self):
        """
        Test searching for structures when all options
        (indoor_pool, sauna, fitness_area) are set to True.

        It should return a list of structures meeting the specified criteria.
        """
        params = {
            'indoor_pool': 'True',
            'sauna': 'True',
            'fitness_area': 'True'
        }
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_search_with_no_option_true(self):
        """
        Test searching for structures
        when all options (indoor_pool, sauna, fitness_area) are set to False.

        It should return an empty list as no structures meet
        the specified criteria.
        """
        params = {
            'indoor_pool': 'False',
            'sauna': 'False',
            'fitness_area': 'False'
        }
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_search_with_only_covered_pool_true(self):
        """
        Test searching for structures with only the
        'indoor_pool' option set to True.

        It should return a list of structures with covered pools.
        """
        params = {
            'indoor_pool': 'True',
            'sauna': 'False',
            'fitness_area': 'False'
        }
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_search_with_only_sauna_true(self):
        """
        Test searching for structures with only the 'sauna'
        option set to True.

        It should return a list of structures with saunas.
        """
        params = {
            'indoor_pool': 'False',
            'sauna': 'True',
            'fitness_area': 'False'
        }
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_search_with_only_fitness_area_true(self):
        """
        Test searching for structures with only the 'fitness_area'
        option set to True.

        It should return a list of structures with fitness areas.
        """
        params = {
            'indoor_pool': 'False',
            'sauna': 'False',
            'fitness_area': 'True'
        }
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_search_with_only_covered_pool_and_sauna_true(self):
        """
        Test searching for structures with only the 'indoor_pool'
        and 'sauna' options set to True.

        It should return a list of structures with covered pools and saunas.
        """
        params = {
            'indoor_pool': 'True',
            'sauna': 'True',
            'fitness_area': 'False'
        }
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_search_with_only_covered_pool_and_fitness_area_true(self):
        """
        Test searching for structures with 'indoor_pool' and
        'fitness_area' set to True.

        It should return a list of structures with covered pools
        and fitness areas.
        """
        params = {
            'indoor_pool': 'True',
            'sauna': 'False',
            'fitness_area': 'True'
        }
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_search_with_only_sauna_and_fitness_area_true(self):
        """
        Test searching for structures with 'sauna'
        and 'fitness_area' set to True.

        It should return a list of structures with saunas and fitness areas.
        """
        params = {
            'indoor_pool': 'False',
            'sauna': 'True',
            'fitness_area': 'True'
        }
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_search_with_invalid_parameters(self):
        """
        Test handling of invalid parameters in the search.

        It should return a validation error (status code 422) as
        FastAPI rejects invalid parameters.
        """
        params = {'sauna': 'InvalidValue'}
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 422)
        result = response.json()
        self.assertEqual(result['detail'][0]['msg'], 'value could not be parsed to a boolean')

    def test_search_with_invalid_boolean_parameters(self):
        """
        Test handling of invalid boolean parameters in the search.

        It should return a validation error (status code 422) as
        FastAPI rejects invalid boolean parameters.
        """
        params = {'indoor_pool': 'InvalidValue'}
        response = self.client.get('/search_structures', params=params)
        self.assertEqual(response.status_code, 422)
        result = response.json()
        self.assertEqual(result['detail'][0]['msg'], 'value could not be parsed to a boolean')



class TestApp(unittest.TestCase):
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
    assert not df.isna().any().any()


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


def test_valid_entries_and_input():
    """
    Checks if the function handles known valid inputs properly.
    """
    # Test valid entries
    result_valid_entries = essential_services_periphery("True", "True")
    assert isinstance(result_valid_entries, list)
    assert all(isinstance(item, dict) for item in result_valid_entries)

    # Test valid input
    result_valid_input = essential_services_periphery("True", "True")
    assert isinstance(result_valid_input, list)
    assert len(result_valid_input) >= 0


def test_invalid_entries_and_input():
    """
    Validates the behavior when known invalid inputs are provided.
    """
    # Test invalid entries
    result_invalid_entries = essential_services_periphery("Invalid", "Invalid")
    assert result_invalid_entries == []

    # Test invalid input
    result_invalid_input = essential_services_periphery("NotTrue", "NotTrue")
    assert isinstance(result_invalid_input, list)
    assert len(result_invalid_input) == 0


def test_edge_and_boolean_cases():
    """
    Examines the behavior of the function with edge input and boolean values.
    """
    # Test edge cases
    result_edge_cases = essential_services_periphery("False", "False")
    assert isinstance(result_edge_cases, list)
    assert len(result_edge_cases) == 0

    # Test edge cases with boolean values
    result_true_false = essential_services_periphery("True", "False")
    result_false_true = essential_services_periphery("False", "True")
    assert isinstance(result_true_false, list)
    assert isinstance(result_false_true, list)


def test_corner_and_specific_cases():
    """
    Validates the handling of corner cases by the function.
    """
    # Test general corner cases
    result_general_corner = essential_services_periphery("true", "false")
    assert isinstance(result_general_corner, list)
    assert all(isinstance(item, dict) for item in result_general_corner)

    # Test specific corner cases
    result_specific_corner = essential_services_periphery("", "Vero")
    assert isinstance(result_specific_corner, list)


def test_empty_and_extreme_values():
    """
    Verifies the behavior when empty strings and extreme inputs are provided.
    """
    # Test empty inputs
    result_empty_inputs = essential_services_periphery("", "")
    assert result_empty_inputs == []

    # Test extreme values
    result_extreme_values = essential_services_periphery("True", "True")
    assert isinstance(result_extreme_values, list)
    assert len(result_extreme_values) < 1000


def test_data_format():
    """
    Ensures that the returned data has specific keys as expected.
    """
    result_data_format = essential_services_periphery("False", "True")
    assert all('DENOMINAZIONE' in item for item in result_data_format)
    assert all('INDIRIZZO' in item for item in result_data_format)
    assert all('NUMERO CIVICO' in item for item in result_data_format)
    assert all('COMUNE' in item for item in result_data_format)
    assert all('CAP' in item for item in result_data_format)
    assert all('PROVINCIA' in item for item in result_data_format)
    assert all('EMAIL' in item for item in result_data_format)


def test_specific_scenario():
    """
    Test a specific scenario to ensure proper handling
    Ensures the result is a list and validates its minimum length.
    """
    result_specific = essential_services_periphery("False", "False")
    assert isinstance(result_specific, list)
    assert len(result_specific) >= 0


@pytest.mark.performance
def test_performance():
    """
    Evaluates the performance of the function under a specific load assumption.
    """
    result_performance = essential_services_periphery("False", "True")
    assert len(result_performance) < 10000


def test_mixed_validations_valid():
    """
    Validates mixed inputs and expected outputs for valid cases.
    """
    # Test mixed valid entries and input
    result_mixed_valid = essential_services_periphery("True", "False")
    assert isinstance(result_mixed_valid, list)
    assert all(isinstance(item, dict) for item in result_mixed_valid)


def test_mixed_validations_invalid():
    """
    Validates mixed inputs and expected outputs for invalid cases.
    """
    # Test mixed invalid entries and input
    result_mixed_invalid = essential_services_periphery("Invalid", "True")
    assert result_mixed_invalid == []


def test_no_filters():
    """
    Evaluates behavior when no filters are applied.
    """
    # Test when no filters are applied (using default string values)
    result_no_filters = essential_services_periphery(air_conditioning="False",
                                                     pets_allowed="False")
    assert isinstance(result_no_filters, list)


def test_different_inputs_and_lengths():
    """
    Test different inputs and checks the lengths of the results.
    """
    # Test different inputs and ensure results have appropriate lengths
    input_combinations = [
        ("True", "False"),
        ("False", "True"),
        ("True", "True"),
        ("False", "False"),
        ("Invalid", "Invalid"),
        ("NotTrue", "NotTrue"),
        ("", "Vero"),
        ("", ""),
        ("true", "false")
    ]

    expected_lengths = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for index, (input1, input2) in enumerate(input_combinations):
        result = essential_services_periphery(input1, input2)
        assert isinstance(result, list)
        assert len(result) == expected_lengths[index], (
            f"Test failed for inputs: {input1}, {input2}")


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_find_hotel_near_transports(self):
        # Typology 'hotel' with both train station and highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "ALBERGO",
            "train_station": "Yes",
            "highway": "Yes"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_hostel_near_transports(self):
        # Typology 'hostel' with both train station and highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "OSTELLO",
            "train_station": "Yes",
            "highway": "Yes"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_find_rooms_near_transports(self):
        # Typology 'rooms' with train station and no highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "CAMERE",
            "train_station": "Yes",
            "highway": "No"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_country_house_no_transports(self):
        # Typology 'country house' with neither train station nor highway
        response = self.client.get("/find_hotels_near_transports", params={
             "selected_typology": "COUNTRY_HOUSE",
             "train_station": "No",
             "highway": "No"
        })
        result = response.json()
        self.assertIsInstance(result, list)

    def test_get_typology_empty_data(self):
        # Test when there is no data for typologies
        response = self.client.get("/get_typology")
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, str)

    def test_find_country_house(self):
        # Typology 'COUNTRY_HOUSE' with neither train station nor highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "COUNTRY_HOUSE",
            "train_station": "No",
            "highway": "No"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_hotels_near_transports_with_highway(self):
        # Trying with the typology 'hotel' near the highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "ALBERGO",
            "train_station": "No",
            "highway": "Yes"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_holiday_apartments_near_train_station(self):
        # Typology 'holiday apartments' near the train station
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "APPARTAMENTI_VACANZE",
            "train_station": "Yes",
            "highway": "No"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_bed_and_breakfast_near_train_station(self):
        # Typology 'bed and breakfast' near the train station
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "BED_AND_BREAKFAST",
            "train_station": "Yes",
            "highway": "No"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_resort_with_fitness_area(self):
        # 'Holiday apartments' with neither train station nor highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "APPARTAMENTI_VACANZE",
            "train_station": "No",
            "highway": "No",
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_hostel_near_highway(self):
        # Typology 'hostel' near the highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "OSTELLO",
            "train_station": "No",
            "highway": "Yes"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()


# Test to check if the endpoint returns data for valid filters
# Assuming there is data for the specified filters
def test_get_structures_with_data():
    response = client.get(
        "/structures",
        params={
            'zone': 'dolomiti',
            'parking': 'Vero',
            'restaurant': 'Vero'
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
            'zone': 'nonexistent',
            'parking': 'Falso',
            'restaurant': 'Falso'
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
            'restaurant': 'Vero',
        }
    )
    assert response.status_code == 422  # Assuming 422 for bad request


# Test to check if the endpoint returns data for a specific zone (dolomiti)
def test_zone_dolomiti():
    response = client.get(
        "/structures",
        params={
            'zone': 'dolomiti',
            'parking': 'Vero',
            'restaurant': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (caorle)
def test_zone_caorle():
    response = client.get(
        "/structures",
        params={'zone': 'caorle', 'parking': 'Falso', 'restaurant': 'Vero'}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (jesolo-eraclea)
def test_zone_jesolo_eraclea():
    response = client.get(
        "/structures",
        params={
            'zone': 'jesolo-eraclea',
            'parking': 'Vero',
            'restaurant': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (bibione)
def test_zone_bibione():
    response = client.get(
        "/structures",
        params={
            'zone': 'bibione',
            'parking': 'Falso',
            'restaurant': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (altopiano-asiago)
def test_zone_altopiano_asiago():
    response = client.get(
        "/structures",
        params={
            'zone': 'altopiano-asiago',
            'parking': 'Vero',
            'restaurant': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (belluno-feltre-alpago)
def test_zone_belluno_feltre_alpago():
    response = client.get(
        "/structures",
        params={
            'zone': 'belluno-feltre-alpago',
            'parking': 'Falso',
            'restaurant': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (cavallino)
def test_zone_cavallino():
    response = client.get(
        "/structures",
        params={
            'zone': 'cavallino',
            'parking': 'Vero',
            'restaurant': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (chioggia)
def test_zone_chioggia():
    response = client.get(
        "/structures",
        params={
            'zone': 'chioggia',
            'parking': 'Falso',
            'restaurant': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (garda)
def test_zone_garda():
    response = client.get(
        "/structures",
        params={
            'zone': 'garda',
            'parking': 'Falso',
            'restaurant': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (padova)
def test_zone_padova():
    response = client.get(
        "/structures",
        params={
            'zone': 'padova',
            'parking': 'Vero',
            'restaurant': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (rovigo)
def test_zone_rovigo():
    response = client.get(
        "/structures",
        params={
            'zone': 'rovigo',
            'parking': 'Falso',
            'restaurant': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (terme-euganee)
def test_zone_terme_euganee():
    response = client.get(
        "/structures",
        params={
            'zone': 'terme-euganee',
            'parking': 'Vero',
            'restaurant': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (treviso)
def test_zone_treviso():
    response = client.get(
        "/structures",
        params={
            'zone': 'treviso',
            'parking': 'Falso',
            'restaurant': 'Falso'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test for a specific zone (venezia)
def test_zone_venezia():
    response = client.get(
        "/structures",
        params={
            'zone': 'venezia',
            'parking': 'Vero',
            'restaurant': 'Vero'
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
