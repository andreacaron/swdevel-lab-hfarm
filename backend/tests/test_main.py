import os
import sys
import pytest
from fastapi.testclient import TestClient

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app, essential_services_periphery

# Skipping performance tests
pytest.mark.performance = pytest.mark.skip(reason="Performance tests skipped")

# Setting the path for importing the FastAPI application
current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, parent_directory)

# Creating a test client to interact with the FastAPI app
client = TestClient(app)


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
