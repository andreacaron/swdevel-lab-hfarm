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

class TestCercaStrutture(unittest.TestCase):

    def test_tutte_opzioni_true(self):
        result = cerca_strutture(piscina_coperta=True, sauna=True, area_fitness=True)
        self.assertIsInstance(result, list)
        

    def test_nessuna_opzione_true(self):
        result = cerca_strutture(piscina_coperta=False, sauna=False, area_fitness=False)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_solo_piscina_coperta_true(self):
        result = cerca_strutture(piscina_coperta=True, sauna=False, area_fitness=False)
        self.assertIsInstance(result, list)
        

    def test_solo_sauna_true(self):
        result = cerca_strutture(piscina_coperta=False, sauna=True, area_fitness=False)
        self.assertIsInstance(result, list)
        

    def test_solo_area_fitness_true(self):
        result = cerca_strutture(piscina_coperta=False, sauna=False, area_fitness=True)
        self.assertIsInstance(result, list)
        

    def test_solo_piscina_coperta_e_sauna_true(self):
        result = cerca_strutture(piscina_coperta=True, sauna=True, area_fitness=False)
        self.assertIsInstance(result, list)
        

    def test_solo_piscina_coperta_e_area_fitness_true(self):
        result = cerca_strutture(piscina_coperta=True, sauna=False, area_fitness=True)
        self.assertIsInstance(result, list)
        

    def test_solo_sauna_e_area_fitness_true(self):
        result = cerca_strutture(piscina_coperta=False, sauna=True, area_fitness=True)
        self.assertIsInstance(result, list)
        

    def test_tutte_opzioni_false(self):
        result = cerca_strutture(piscina_coperta=False, sauna=False, area_fitness=False)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_piscina_coperta_true_e_altre_opzioni_false(self):
        result = cerca_strutture(piscina_coperta=True, sauna=False, area_fitness=False)
        self.assertIsInstance(result, list)
        

    def test_sauna_true_e_altre_opzioni_false(self):
        result = cerca_strutture(piscina_coperta=False, sauna=True, area_fitness=False)
        self.assertIsInstance(result, list)
        

    def test_area_fitness_true_e_altre_opzioni_false(self):
        result = cerca_strutture(piscina_coperta=False, sauna=False, area_fitness=True)
        self.assertIsInstance(result, list)
        

   


if __name__ == '__main__':
    unittest.main()




