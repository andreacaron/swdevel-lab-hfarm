import os
import sys
from fastapi.testclient import TestClient
import pandas as pd
from app.main import app
from app.main import cerca_strutture
import unittest


# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
 """

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
        result = cerca_strutture(piscina_coperta=True,
                                 sauna=True,
                                 area_fitness=True)
        self.assertIsInstance(result, list)

    def test_no_option_true(self):
        """
        Verify if the cerca_strutture function returns an empty list
        when all options are set to False.
        """
        result = cerca_strutture(piscina_coperta=False,
                                 sauna=False,
                                 area_fitness=False)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_only_covered_pool_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'piscina_coperta' option is set to True.
        """
        result = cerca_strutture(piscina_coperta=True,
                                 sauna=False,
                                 area_fitness=False)
        self.assertIsInstance(result, list)

    def test_only_sauna_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'sauna' option is set to True.
        """
        result = cerca_strutture(piscina_coperta=False,
                                 sauna=True,
                                 area_fitness=False)
        self.assertIsInstance(result, list)

    def test_only_fitness_area_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'area_fitness' option is set to True.
        """
        result = cerca_strutture(piscina_coperta=False,
                                 sauna=False,
                                 area_fitness=True)
        self.assertIsInstance(result, list)

    def test_only_covered_pool_and_sauna_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'piscina_coperta' and 'sauna' options are set to True.
        """
        result = cerca_strutture(piscina_coperta=True,
                                 sauna=True,
                                 area_fitness=False)
        self.assertIsInstance(result, list)

    def test_only_covered_pool_and_fitness_area_true(self):
        """
        Verify if the cerca_strutture function returns a list
        with 'piscina_coperta' and 'area_fitness' set to True.
        """
        result = cerca_strutture(piscina_coperta=True,
                                 sauna=False,
                                 area_fitness=True)
        self.assertIsInstance(result, list)

    def test_only_sauna_and_fitness_area_true(self):
        """
        Verify if the cerca_strutture function returns a list
        when only the 'sauna' and 'area_fitness' options are set to True.
        """
        result = cerca_strutture(piscina_coperta=False,
                                 sauna=True,
                                 area_fitness=True)
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()


class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_find_albergo(self):
        # Typology 'albergo' with both train station and highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "ALBERGO",
            "stazione": "Yes",
            "autostrada": "Yes"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_ostello(self):
        # Typology 'ostello' with both train station and highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "OSTELLO",
            "stazione": "Yes",
            "autostrada": "Yes"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_find_camere(self):
        # Typology 'camere' with train station and no highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "CAMERE",
            "stazione": "Yes",
            "autostrada": "No"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_country_house_no_transports(self):
        # Typology 'country house' with neither the station nor the motorway
        response = self.client.get("/find_hotels_near_transports", params={
             "selected_typology": "COUNTRY_HOUSE",
             "stazione": "No",
             "autostrada": "No"
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
        # Typology 'COUNTRY_HOUSE' with neither the station nor the highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "COUNTRY_HOUSE",
            "stazione": "No",
            "autostrada": "No"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_hotels_near_transports_with_highway(self):
        # Trying with the typology 'Hotel' near the highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "ALBERGO",
            "stazione": "No",
            "autostrada": "Yes"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_appartamenti_vacanze(self):
        #
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "APPARTAMENTI_VACANZE",
            "stazione": "Yes",
            "autostrada": "No"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_bed_and_breakfast(self):
        # Typology 'Bed and Breakfast' near the station
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "BED_AND_BREAKFAST",
            "stazione": "Yes",
            "autostrada": "No"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_resort_with_fitness_area(self):
        # Typology 'Holiday apartments' with no train station and highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "APPARTAMENTI_VACANZE",
            "stazione": "No",
            "autostrada": "No",
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)

    def test_find_hostel_near_highway(self):
        # Typology 'Hostel' near the highway
        response = self.client.get("/find_hotels_near_transports", params={
            "selected_typology": "OSTELLO",
            "stazione": "No",
            "autostrada": "Yes"
        })
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
