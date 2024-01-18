# README 

**Group name**: Animal crossers

**Welcome to the Tourist Accommodation Research Project in the Veneto Region!**

This repository is dedicated to exploring accommodation options, transportation, and essential services available in different areas of the region, providing detailed and useful information for anyone planning a trip to this fascinating part of Italy!

## Project Purpose

Our goal is to provide a comprehensive overview of accommodation options, with a specific focus on crucial aspects such as location, provided services, and access to transportation. We have structured the project into various sections, each focusing on a key aspect of the research:

### Feature 1 - Essentials

We explore available accommodation options in the seaside areas that may or may not have restaurants and parking.

### Feature 2 - Transportation explorer
We search for accommodation options near train stations and with highway access.

### Feature 3 - Peripherical BnB

We recommend bed and breakfasts in the suburbs that offer essential services such as air conditioning and accept pets to ensure a comfortable stay.

### Feature 4 - Wellness explorer

We investigate accommodation facilities with an indoor pool, sauna, and fitness area in the fair zone, catering to those seeking a more complete experience.

### Feature 5 - Suburbs explorer
We identify accommodations in the outskirts offering services in English, French, German, and Spanish.

## Data Source

The data used in this project comes from the official website of Veneto region. This source provides a detailed list of tourist accommodation facilities in the region, ensuring accuracy and information updates. This is the link to access the dataset:
https://dati.veneto.it/content/elenco-delle-strutture-ricettive-turistiche-della-regione-veneto

## Libraries

- **FastAPI**: A Python web framework used for developing web applications, providing tools, libraries, and technologies for building web applications.
  - **TestClient(FastAPI)**: A class provided by the FastAPI testing utilities. It is used to verify the functionality of different endpoints through various test cases.
  - **fastapi.responses**: Provides various response classes for creating API responses.
  - **fastapi.middleware.cors**: Middleware for handling Cross-Origin Resource Sharing (CORS) in FastAPI applications.
  - **pydantic**: A data validation and settings management library for Python.
  - **uvicorn**: ASGI server that runs FastAPI applications.

- **Flask**: A Python web framework used for developing web applications, providing tools, libraries, and technologies for building web applications.
  - **render_template**: A Flask function for rendering HTML templates.
  - **FlaskForm**: A class from Flask-WTF for creating forms in Flask applications.
  - **StringField, SubmitField, SelectField**: Classes from WTForms for creating form fields.

- **Pandas**: A powerful data manipulation and analysis library for Python.
- **Requests**: An HTTP library that simplifies making HTTP requests to interact with web services and APIs.
- **json**: A module in Python that facilitates encoding and decoding JSON data, commonly used for data interchange between a server and a web application.
- **Flask-WTF**: An extension for Flask that integrates WTForms, a flexible forms validation and rendering library, simplifying form creation and validation in Flask applications.
- **os**: Python module for interacting with the operating system, facilitating file system navigation, environment variable management, and system command execution.
- **sys**: Python module offering access to interpreter-specific variables, enabling manipulation of the runtime environment, including command-line arguments.
- **pytest**: Python testing framework for easy and scalable unit testing
- **unittest***: Built-in Python unit testing framework providing test discovery, fixtures, and a test runner; organizes tests into classes that inherit from unittest.TestCase.


## Helper Modules:

We developed everythin in one module, main, both in the backend and in the frontend.

**1. Essentials Feature:**
  - Backend: structures() function in `main.py`
  - Frontend: `essentials.html` template and Flask routes in `main.py`

**2. Transportation Explorer Feature:**
  - Backend: find_hotels_near_transport() function in `transportation_backend.py`
  - Frontend: `transports.html` template and Flask routes in `main.py`

**3. Peripherical BnB Feature:**
  - Backend: essential_services_periphery() function in `peripherical_bnb_backend.py`
  - Frontend: `extras.html` template and Flask routes in `main.py`

**4. Wellness Explorer Feature:**
  - Backend: search_structures() function in `main.py`
  - Frontend: `luxuries.html` template and Flask routes in `main.py`

**5. Suburbs Explorer Feature:**
  - Backend: find_structures_suburb() function in `suburbs_backend.py`
  - Frontend: `languages.html` template and Flask routes in `main.py`


## HOME PAGE 
The `home_page.html` code represents the home page of the website.

This HTML template serves as the foundation for the Animal Crossers web application. The template utilizes Bootstrap, a popular front-end framework, to ensure a responsive and visually appealing design. The structure and components are tailored to accommodate the various features and pages of the Animal Crossers project.

**Template Structure**

- Meta Tags
Charset and Viewport: Ensures proper character encoding and sets the viewport for responsiveness.

- CSS Libraries
1. Bootstrap CSS: Provides the core styling for the application.
2. Bootstrap Icons: Includes a set of icons for visual elements.
3. Bootstrap Table CSS: Adds styles for displaying tables.

- Title
The title of the page is dynamically set using the Jinja2 templating engine. Each specific page can override the default title.

- Body

JavaScript Libraries
1. jQuery: A JavaScript library for simplified HTML document traversal and manipulation.
2. Bootstrap Bundle JS: Includes Bootstrap's JavaScript plugins.
3. Bootstrap Table JS: Adds functionality for interactive tables.

Custom JavaScript
app.js: A custom JavaScript file for additional functionality. Make sure to link the correct path based on the project structure.

Navigation Bar
1. A responsive navigation bar created using Bootstrap's Navbar component.
2. Animal Crossers logo with a link to the home page.
3. Navigation links for each feature/page of the application.

Content Container
A container div to hold the main content of each page.
The {% block content %}{% endblock %} tags allow specific content to be injected into this section for each page.

## CUSTOMIZED WEB PAGES 
We applied a custumized CSS style to every web page to enhance the visual appeal. These styles are designed for improved aesthetics and can be easily integrated into your project.

The CSS code include styling for the overall page, container, header, subtitle, form, result container, result heading, card, card title, card text, primary button, primary button hover, muted text, and danger text.

Following you will find detailed descriptions of each Feature.


# FEATURE 1 "ESSENTIALS"
*Ilhame Sebbar 891944*

The "Essentials" feature in this FastAPI application aims to provide users with information about available accommodation structures in various zones based on specific criteria, such as the presence of essential services like restaurants and parking.

## BACKEND OVERVIEW
The backend of the application is implemented using FastAPI and relies on Pandas for efficient data manipulation. Accommodation data is read from a CSV file ("dove-alloggiare.csv") during startup. The "structures" endpoint filters the data based on user-specified criteria (zone, parking availability, and restaurant availability) and returns the relevant information in JSON format. The "get_zones" endpoint provides a list of unique zones available in the dataset.


**Tests description**

Different tests have been implemented to ensure the robustness of the "structures" and "get_zones" endpoint. The tests cover various scenarios, including valid and invalid filter parameters, different combinations of true and false values for search criteria, and specific zones. Additionally, tests are in place to verify the correct handling of non-existent zones.


- test_get_structures_with_data(): To test if structures are retrieved successfully with valid criteria.
- test_get_structures_no_data(): To test if an empty list is returned for invalid criteria.
- test_get_zones_not_empty(): To test if unique zones are retrieved successfully.
- test_invalid_filter_parameter(): To test if an invalid filter parameter results in a validation error.
- test_zone_dolomiti(): To test if the specified zone (dolomiti) returns data smoothly.
- test_zone_caorle(): To test if the specified zone (caorle) returns data smoothly.

Did the same for each zone.

## FRONTEND OVERVIEW

This frontend is part of the "Essentials" feature in a web application implemented using Flask. The purpose of the feature is to provide users with information about available accommodation structures in various zones based on specific criteria, such as the presence of essential services like restaurants and parking. This documentation outlines the frontend's structure, form configuration, and how it interacts with the FastAPI backend.

**Code explanation**

The frontend is built using Flask. It includes a form for users to input search criteria, such as zone, restaurant availability, and parking availability. The form is created using Flask-WTF and WTForms. Upon submitting the form, a request is sent to the FastAPI backend to retrieve relevant information based on the user's criteria.



The search form (`SearchForm`) includes the following fields:
- `zone`: A dropdown list for selecting the desired zone.
- `restaurant`: A dropdown list for selecting restaurant availability (Yes/No).
- `parking`: A dropdown list for selecting parking availability (Yes/No).
- `submit`: A submit button to trigger the search.

The Flask application is configured to communicate with the FastAPI backend, whose URL is defined by `FASTAPI_BACKEND_HOST` and used to construct the endpoint URL.


**Internal Page Route**

The `/essentials` route handles the rendering of the 'essentials' page. It retrieves unique zones from the FastAPI backend and populates the dropdown list in the search form dynamically. The user's search criteria are then used to query the backend for relevant information.


**Additional Notes**

- The application assumes the availability of the FastAPI backend at the specified URL.
- Adjustments can be made to the code or configuration based on specific requirements.
- For development purposes, the application runs on host '0.0.0.0' and port 80.


# FEATURE 2 "TRANSPORTATION EXPLORER"
*Martina De Rocco 890739*

The 'Transportation Explorer' function of this FastAPI is designed to assist users in exploring accommodation options in different areas. It offers specific criteria, including the availability of transport-related services, such as proximity to railway stations and highways, allowing users to find accommodation suitable for their transport needs.

## BACKEND OVERVIEW
The backend of ‘Transportation Explorer’  is implemented using FastAPI and makes use of Pandas for efficient data manipulation. During start-up, the accommodation data is read from a CSV file called 'where-lodging.csv'. The 'find_hotels_near_transports' endpoint filters the data according to user-specified criteria (type, presence of railway station and motorway) and returns the relevant information in JSON format. The 'get_typology' endpoint provides a list of unique types available in the dataset.


**Tests description**

This backend application has been thoroughly tested using the unittest framework to ensure the reliability of the `find_hotels_near_transports` and `get_typology` endpoints. Various test cases cover a range of scenarios, including different combinations of valid and invalid parameters for typologies, train stations, and highways.

- test_find_albergo(): Validates the retrieval of 'albergo' type structures with both train station and highway present.
- test_find_ostello(): Checks the handling of 'ostello' type structures with both train station and highway present.
- test_find_camere(): Tests the retrieval of 'camere' type structures with a train station and no highway.
- test_find_country_house_no_transports(): Examines the handling of 'country house' type structures with neither train station nor highway.
- test_get_typology_empty_data(): Ensures proper handling when there is no data for typologies.
- test_find_country_house(): Verifies the retrieval of 'country house' type structures with neither train station nor highway.
- test_find_hotels_near_transports_with_highway(): Tests the search for 'ALBERGO' type structures near the highway.
- test_find_appartamenti_vacanze(): Checks the retrieval of 'APPARTAMENTI_VACANZE' type structures with a train station and no highway.
- test_find_bed_and_breakfast(): Validates the search for 'BED_AND_BREAKFAST' type structures near the train station.
- test_find_resort_with_fitness_area(): Tests the retrieval of 'APPARTAMENTI_VACANZE' type structures with no train station and no highway.
- test_find_hostel_near_highway(): Examines the search for 'OSTELLO' type structures near the highway.


**Usage**

To use the application, follow these steps:
1. Ensure that the CSV file (dove-alloggiare.csv) is present in the specified path in the code.
2. Call the `/find_hotels_near_transports` endpoint with the appropriate parameters for the search.

Unit tests are provided to ensure the correct functioning of the `find_hotels_near_transports` function in various scenarios.



## FRONTEND OVERVIEW

This frontend is an integral part of the "Essentials" feature within a web application developed using Flask. The main objective of this feature is to furnish users with information regarding available accommodation structures in various zones based on specific criteria, such as the presence of essential services like restaurants and parking. This documentation provides insights into the frontend's architecture, form configuration, and its interaction with the FastAPI backend.


**Code explanation**

The frontend is implemented using Flask, incorporating a form that enables users to input search criteria such as zone, restaurant availability, and parking availability. This form is constructed using Flask-WTF and WTForms. Upon form submission, a request is dispatched to the FastAPI backend to retrieve pertinent information based on the user's specified criteria.
The search form (`SearchForm`) includes the following fields:
- Train_station: A dropdown list to select the availability of a nearby railway station (Yes/No).
- Highway: A dropdown list to select the availability of a highway (Yes/No).
- Submit: A submit button to initiate the search.
The Flask application is configured to communicate with the FastAPI backend, and the backend's URL is defined by `FASTAPI_BACKEND_HOST` and used to construct the endpoint URL.


**Find_hotels Page Route**

The `/find_hotels` route manages the rendering of the web page. It dynamically fetches unique zones from the FastAPI backend and populates the dropdown list in the search form. 

The user's search criteria are then employed to query the backend for relevant information.


**Additional Notes**

- The application presupposes the availability of the FastAPI backend at the specified URL.
- Adjustments can be made to the code or configuration to meet specific requirements.
- For development purposes, the application runs on host '0.0.0.0' and port 80.


# FEATURE 3 "PERIPHERICAL BNB"
*Katherin Sofia Diaz Montiel 888716*

This meticulously designed FastAPI-based application specializes in filtering bed and breakfast establishments based on user-specified amenities. It seamlessly integrates both backend and frontend modules through meticulously crafted API endpoints. The backend orchestrates data processing and filtration from a CSV file, ensuring seamless responses to frontend requests.

## BACKEND OVERVIEW

The backbone of this application is the backend module, which manages intricate data functionalities and API handling.

#### `essential_services_periphery(aria_condizionata: str, animali_ammessi: str)`
- **Endpoint**: `/essential_services_periphery`
- **Description**: Executes a refined filtration process to retrieve B&B data based on meticulously chosen amenities in periphery areas.
- **Input Parameters**:
  - `air_conditioning`: Signifies the Air Conditioning preference (string).
  - `pets_allowed`: Represents the Pets Allowed preference (string).
- **Functionality**:
  - Meticulously reads and processes BED AND BREAKFAST data stored in the CSV file (`dove-alloggiare.csv`).
  - Impeccably filters BED AND BREAKFASTs situated in periphery areas based on the discerning selection of amenities made by users.
  - Presents a refined dataset of BED AND BREAKFASTs, encapsulating only the most pertinent information.

**Tests description**

The project boasts an exhaustive suite of tests meticulously crafted to scrutinize application functionality and reliability.

***Functionality tests***

- test_valid_entries_and_input(): Checks if the function handles known valid inputs properly.
  - Expected Outcome: Verifies retrieval of a specific dataset aligning with the given valid input conditions.


- test_invalid_entries_and_input(): Validates the behavior when known invalid inputs are provided.
  - Expected Outcome: Expects an empty dataset or appropriate error response indicating invalid input handling.


- test_edge_and_boolean_cases(): Examines the function's behavior with edge/boundary input values and boolean values.
  - Expected Outcome: Verifies appropriate filtering of B&Bs based on edge values.


- test_corner_and_specific_cases(): Validates the handling of corner cases by the function.
  - Expected Outcome: Ensures consistent processing of preferences regardless of case sensitivity.


- test_empty_and_extreme_values(): Verifies the behavior with empty strings and extreme inputs in preferences.
  - Expected Outcome: Checks functionality without compromising, possibly returning an empty dataset.


- test_data_format(): Ensures the returned dataset adheres to specific keys as expected.
  - Expected Outcome: Verifies dataset compliance with specified data formats.


- test_specific_scenario(): Tests a specific scenario to ensure proper handling of essential services periphery function.
  - Expected Outcome: Expects the function to return a list and validates its length.


- test_mixed_validations_valid(): Validates mixed inputs and expected outputs for valid cases.
  - Expected Outcome: Expects a list of dictionaries for all items in the result.


- test_mixed_validations_invalid(): Validates mixed inputs and expected outputs for invalid cases.
  - Expected Outcome: Expects an empty list for invalid mixed inputs.


- test_no_filters(): Evaluates behavior when no filters are applied.
  - Expected Outcome: Expects a list as the result when default string values are used for filtering.


- test_different_inputs_and_lengths(): Tests different inputs and verifies the lengths of the results based on combinations.
  - Expected Outcome: Checks and confirms the expected lengths of result lists for different input combinations.


***Performance Tests***

- test_performance(): Evaluates the function's performance under a specific load assumption.
  - Expected Outcome: Verifies responsiveness and efficiency under increased simulated load, maintaining acceptable response times for B&B queries.


## FRONTEND OVERVIEW

The frontend module delivers an immaculate user interface, meticulously crafted to facilitate seamless interaction with the application.

The frontend is implemented using Flask and includes HTML, WTForms, and CSS components. The `extras.html` template and the Flask routing in `main.py` deliver an engaging and functional user experience.
The `extras.html` template provides a user-friendly form allowing users to specify amenities and view meticulously filtered results. This form is powered by Flask-WTF and interacts with the backend.
The Flask application (segment from `main.py`) includes routes (`/extras`, `/display_results`) to handle form submissions and display results. These routes communicate with the FastAPI backend (`essential_services_periphery` endpoint) to retrieve and display filtered BED AND BREAKFAST information.


# FEATURE 4 "WELLNESS EXPLORER"
*Andrea Caron 891814*

This section provides a comprehensive overview of the "Wellness Explorer" feature, detailing both the backend and frontend components of the accommodation search application.

## BACKEND OVERVIEW
The backend is implemented using the FastAPI framework in Python.

The application reads accommodation data from a CSV file ("dove-alloggiare.csv") and transforms it into a Pandas DataFrame. The "cerca_strutture" function filters structures based on user-specified criteria such as the availability of an indoor pool, sauna, and fitness area. The function efficiently leverages Pandas DataFrame operations for effective filtering.

**Tests description**

To ensure the robustness of the application, a suite of unit tests has been implemented using the FastAPI "TestClient" and the "unittest" module. These tests cover various scenarios, including different combinations of true and false values for search criteria.

- Search with All Options True: validates that the endpoint returns a list of structures meeting the specified criteria when all options (indoor pool, sauna, fitness area) are set to `True`.

- Search with No Option True: ensures that an empty list is returned when all options (indoor pool, sauna, fitness area) are set to `False`, indicating no structures meet the specified criteria.

- Search with Only Covered Pool True: verifies that the endpoint returns a list of structures with covered pools when only the 'indoor_pool' option is set to `True`.

- Search with Only Sauna True: validates that the endpoint returns a list of structures with saunas when only the 'sauna' option is set to `True`.

- Search with Only Fitness Area True: ensures that the endpoint returns a list of structures with fitness areas when only the 'fitness_area' option is set to `True`.

- Search with Only Covered Pool and Sauna True: verifies that the endpoint returns a list of structures with covered pools and saunas when both 'indoor_pool' and 'sauna' options are set to `True`.

- Search with Only Covered Pool and Fitness Area True: validates that the endpoint returns a list of structures with covered pools and fitness areas when both 'indoor_pool' and 'fitness_area' options are set to `True`.

- Search with Only Sauna and Fitness Area True: ensures that the endpoint returns a list of structures with saunas and fitness areas when both 'sauna' and 'fitness_area' options are set to `True`.


## FRONTEND OVERVIEW

The frontend is built using Flask, a web framework for Python, and facilitates user input, communication with the FastAPI backend, and the presentation of search results.


**Code explanation**

- **Form Creation**: An instance of the SearchForm class is created to handle user input.
- **Form Validation**: If the form is submitted and valid, input data is retrieved, and a URL for the FastAPI backend is constructed.
- **FastAPI Backend Request**: A GET request is made to the FastAPI backend using the constructed URL. Exceptions are caught, and an error message is generated if there are issues with the request.
- **Data Parsing**: If the request is successful, JSON data is parsed from the FastAPI response.
- **Rendering**: The data, along with the form and error message, is rendered on the "luxuries.html" template.


# FEATURE 5 "SUBURBS EXPLORER"
*Samira Satour 888619*

This section will give you an overview of the "Suburbs Explorer" feature, which gives information about available accommodation structures in the suburb zone based on languages preferences, in particular English, French, German, and Spanish.

## BACKEND OVERVIEW
Data is collected from the CSV file called "dove-alloggiare.csv" and transformed into a Pandas DataFrame called "df_suburb" where missing values are substituted with an empty string.

Two functions were created: 

**Find Structures in Suburb**

- Endpoint: `/find_structures_suburb`
- Parameters:
    - `Typology`: Type of accommodation.
    - `English`, `French`, `German`, `Spanish`: Values indicating language support.
- Usage: Returns relevant accommodation information based on specified criteria chosen by the user, like the typology of accommodation and the language.


**Get typology list**

- Endpoint: `/get_typology`
- Usage: Returns a JSON list of unique accommodation types available.


**Tests description**

The testing suite is written using pytest and is designed to verify the functionality of the FastAPI backend. Two types of tests are carried out: the first one is on the function `/find_structures_suburb` while the second one creates a Class of tests called `TestSearchStructures`.

Test Cases for `/find_structures_suburb`:

- test_suburb_albergo_lang: Verifies the functionality of retrieving Albergo structures with all language preferences set to 'True'.
- test_suburb_albergo_nolang: Verifies the functionality of retrieving Albergo structures with all language preferences set to 'False'.
- test_suburb_bed_and_breakfast: Tests the retrieval of Bed and Breakfast structures with all language preferences set to 'True'.
- test_suburb_residence: Tests the retrieval of Residence structures with all language preferences set to 'True'.
- test_suburb_coutry_house: Tests the retrieval of Country House structures with only English set to 'True'.
- test_suburb_rifugio: Tests the retrieval of Rifugio structures with French set to 'False'.
- test_suburb_countryhouse: Tests the scenario when an invalid typology is provided.
- test_suburb_no_results: Tests when there are no results for the specified criteria.
- test_suburb_missing_values: Verifies that the dataframe does not contain missing values after filling them with empty strings.

Test Cases for `TestSearchStructures` Class:

- test_casa_vacanze: Verifies the functionality of find_structures_suburb for the 'CASA PER VACANZE' typology with all language preferences set to 'True', except German set to 'False'.
- test_ostello: Verifies the functionality of find_structures_suburb for the 'OSTELLO' typology with only English set to 'True'.
- test_bed_and_breakfast: Verifies the functionality of find_structures_suburb for the 'BED AND BREAKFAST' typology with only Spanish set to 'True'.


## FRONTEND OVERVIEW

The frontend application is designed to provide users with a user-friendly interface to search for accommodation structures in a suburban area.

It interacts with the FastAPI backend, which exposes relevant endpoints for querying accommodation data.


- The search form allows users to specify the desired type of structure and language preferences (English, French, German, and Spanish).
- Upon submitting the search form, the results are displayed on the page, showing relevant information about the found accommodation structures, such as their name and their contact details.


**Usage**

To integrate the frontend with the backend and enable the research:

1. Ensure that the Flask backend is running and accessible.
2. Modify the FASTAPI_BACKEND_HOST variable with the appropriate FastAPI backend URL.
3. Implement the frontend code within your web application.
4. Create an HTML template (e.g., "periferia.html") to display the search form and results.
5. Customize the form fields and design as needed to fit your application's requirements.



## Usage

To use the application, follow these steps:
1. Ensure that the CSV file ("dove-alloggiare.csv") is present in the specified path in the code;
3. Tests are provided to ensure the correct functioning of the functions in various scenarios.

## IMPORTANT ANNOTATIONS

- To run the different tests please write in the terminal pytest --cov=app --cov-report=html tests/ and also this command coverage report -m, to ensure that all our tests cover all the lines of our codes.

- pycodestyle has been runned in the terminal of these modules:
1. main.py -backend
2. test_main.py -backend
3. main.py -frontend
**Remark**: no pep8 errors were found except for this one in test_main.py: *E402 module level import not at top of file*
We could not fix it because it was necessary to keep that order of code lines otherwise the 'import app' command would have caused an unsurpessable error.

- The developed tests comprehend the use of both pytest and unittest, since each member of the group used the one that fitted better with his/her expectations and with the developed code.

- pydoc -w has been runned in the terminal in both main.py for the backend and frontend to ensure that the documentation was appropriate.

- The different html modules in the frontend are named accordingly with their main funcions.
eg: essentials.html is the web page which displays the Flask route for the essentials services in the Veneto region for the different allocations.

- The images in the Web Page are linked to the owners. We **do not own them**.

- The work was equally splitted among the different group members.

- Tool used for the Software Project Development:
1. Whatsapp
2. Google doc
3. Github
4. Github Desktop
5. Docker
6. Terminal using git


# CONCLUSION
In conclusion, this project aims to facilitate trip planning in the Veneto region by offering a comprehensive guide to accommodation options and related services. The combination of data exploration, powerful Python libraries, and a user-friendly web interface ensures a valuable resource for travelers. We welcome contributions and feedback to enhance the project's utility and accuracy. Happy exploring!
