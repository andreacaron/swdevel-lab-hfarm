**INTRODUCTION FEATURE 4 "WELLNESS EXPLORER"**

The following code is part a project implemented using the FastAPI framework in Python. The purpose of the feature is to create a web application for searching accomodation structures based on specific criteria, such as the presence of an indoor pool, sauna, and fitness area. The main function called "cerca_strutture" takes the search criteria as input and returns a list of structures that meet these criteria.

The project relies on the following Python libraries:
- FastAPI: a modern, fast web framework for building APIs;
- TestClient(FastAPI): a testing utility provided by FastAPI for simulating HTTP requests;
- Pandas: a powerful data manipulation library;

*BACKEND DESCRIPTION*

The application reads accommodation data from a CSV file ("dove-alloggiare.csv") and transforms it into a Pandas DataFrame. Specific fields are converted to strings, and missing values are handled. The "cerca_strutture" function filters structures based on user-specified criteria such as the availability of an indoor pool, sauna, and fitness area. The function leverages Pandas DataFrame operations for efficient filtering.

*TESTS DESCRIPTION*

To ensure the robustness of the application, a suite of unit tests has been implemented using the FastAPI "TestClient" and the "unittest" module. These tests cover various scenarios, including different combinations of true and false values for search criteria.
The individual tests are described below:
- test_all_options_true: verify if the function returns a list when all options are set to True;
- test_no_option_true: verify if the function returns an empty list when all options are set to False;
- test_only_indoor_pool_true: verify if the function returns a list when only the "indoor pool" option is set to True;
- test_only_sauna_true: Verify if the function returns a list when only the 'sauna' option is set to True.
- test_only_fitness_area_true: Verify if the function returns a list when only the 'fitness_area' option is set to True.
- test_only_indoor_pool_and_sauna_true: Verify if the function returns a list when only the 'indoor_pool' and 'sauna' options are set to True.
- test_only_indoor_pool_and_fitness_area_true: Verify if the function returns a list when only the 'indoor_pool' and 'fitness_area' options are set to True.
- test_only_sauna_and_fitness_area_true: Verify if the function returns a list when only the 'sauna' and 'fitness_area' options are set to True.

*USAGE*

To use the application, follow these steps:
1. Ensure that the CSV file ("dove-alloggiare.csv") is present in the specified path in the code;
2. Call the "/cerca_strutture" endpoint with the appropriate parameters for the search;
3. Unit tests are provided to ensure the correct functioning of the "cerca_strutture" function in various scenarios;






