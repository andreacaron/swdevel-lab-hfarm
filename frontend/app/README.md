**INTRODUCTION FEATURE 4 "WELLNESS EXPLORER"**

This section provides an overview of the frontend components responsible for enabling users to interact with the accommodation search functionality. The frontend is built using Flask, a web framework for Python, and facilitates user input, communication with the FastAPI backend, and the presentation of search results.

*DEPENDENCIES*

- Flask: A web framework for Python that simplifies the development of web applications;
- Requests: An HTTP library for making requests to external APIs; 

*CODE EXPLANATION*

- Form Creation: An instance of the SearchForm class is created to handle user input;
- Form Validation: If the form is submitted and is valid, the input data is retrieved, and a URL for the FastAPI backend is constructed with the user's input;
- FastAPI Backend Request: A GET request is made to the FastAPI backend using the constructed URL. Exceptions are caught, and an error message is generated if there are issues with the request;
- Data Parsing: If the request is successful, JSON data is parsed from the FastAPI response;
- Rendering: The data, along with the form and error message, is rendered on the "search.html" template;

*USAGE* 

To integrate the frontend with the backend and enable accommodation structure searches:

1. Ensure that the Flask backend is running and accessible.
2. Modify the FASTAPI_BACKEND_HOST variable with the appropriate FastAPI backend URL.
3. Implement the frontend code within your web application.
4. Create an HTML template (e.g., "search.html") to display the search form and results.
5. Customize the form fields and design as needed to fit your application's requirements.

