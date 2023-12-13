import os
import sys
from fastapi.testclient import TestClient
import pandas as pd

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app
# Importa il modulo contenente la tua funzione
from app.main import cerca_strutture
import unittest


"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
 """

client = TestClient(app)

import unittest

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



