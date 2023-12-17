import os
import sys
import pytest
from fastapi.testclient import TestClient
import pandas as pd
import unittest
import pandas as pd

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app, essential_services_periphery, cerca_strutture, df_suburb, find_structures_suburb

# Create a TestClient instance for testing API endpoints
# Skipping performance tests
pytest.mark.performance = pytest.mark.skip(reason="Performance tests skipped")

# Creating a test client to interact with the FastAPI app
client = TestClient(app)


class TestSearchStructures(unittest.TestCase):
    """
    This class contains tests for the cerca_strutture function.
    Make sure to adapt the documentation and imports to your needs.
    """

    def test_all_options_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when all options are set to True.
        """
        result = cerca_strutture(piscina_coperta=True, sauna=True, area_fitness=True)
        self.assertIsInstance(result, list)

    def test_no_option_true(self):
        """
        Verify if the cerca_strutture function returns an empty list
        when all options are set to False.
        """
        result = cerca_strutture(piscina_coperta=False, sauna=False, area_fitness=False)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_only_covered_pool_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'piscina_coperta' option is set to True.
        """
        result = cerca_strutture(piscina_coperta=True, sauna=False, area_fitness=False)
        self.assertIsInstance(result, list)

    def test_only_sauna_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'sauna' option is set to True.
        """
        result = cerca_strutture(piscina_coperta=False, sauna=True, area_fitness=False)
        self.assertIsInstance(result, list)

    def test_only_fitness_area_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'area_fitness' option is set to True.
        """
        result = cerca_strutture(piscina_coperta=False, sauna=False, area_fitness=True)
        self.assertIsInstance(result, list)

    def test_only_covered_pool_and_sauna_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'piscina_coperta' and 'sauna' options are set to True.
        """
        result = cerca_strutture(piscina_coperta=True, sauna=True, area_fitness=False)
        self.assertIsInstance(result, list)

    def test_only_covered_pool_and_fitness_area_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'piscina_coperta' and 'area_fitness' options are set to True.
        """
        result = cerca_strutture(piscina_coperta=True, sauna=False, area_fitness=True)
        self.assertIsInstance(result, list)

    def test_only_sauna_and_fitness_area_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'sauna' and 'area_fitness' options are set to True.
        """
        result = cerca_strutture(piscina_coperta=False, sauna=True, area_fitness=True)
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()



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

# TEST 1
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


# TEST 2
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


# TEST 3
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


# TEST 4
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


# TEST 5
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


# TEST 6
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


# TEST 7
def test_specific_scenario():
    """
    Test a specific scenario to ensure proper handling
    Ensures the result is a list and validates its minimum length.
    """
    result_specific = essential_services_periphery("False", "False")
    assert isinstance(result_specific, list)
    assert len(result_specific) >= 0


# TEST 8
@pytest.mark.performance
def test_performance():
    """
    Evaluates the performance of the function under a specific load assumption.
    """
    result_performance = essential_services_periphery("False", "True")
    assert len(result_performance) < 10000


# TEST 9
def test_mixed_validations_valid():
    """
    Validates mixed inputs and expected outputs for valid cases.
    """
    # Test mixed valid entries and input
    result_mixed_valid = essential_services_periphery("True", "False")
    assert isinstance(result_mixed_valid, list)
    assert all(isinstance(item, dict) for item in result_mixed_valid)


# TEST 10
def test_mixed_validations_invalid():
    """
    Validates mixed inputs and expected outputs for invalid cases.
    """
    # Test mixed invalid entries and input
    result_mixed_invalid = essential_services_periphery("Invalid", "True")
    assert result_mixed_invalid == []


# TEST 11
def test_no_filters():
    """
    Evaluates behavior when no filters are applied.
    """
    # Test when no filters are applied (using default string values)
    result_no_filters = essential_services_periphery(aria_condizionata="False",
                                                     animali_ammessi="False")
    assert isinstance(result_no_filters, list)


# TEST 12
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
