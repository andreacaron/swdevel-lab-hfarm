**INTRODUCTION FEATURE 3: "BED AND BREAKFAST FILTER"**

This section highlights the integration of the frontend components, empowering users to interact with accommodation search functionality. Built on Flask, a Python-based web framework, it enables user input, communicates with a FastAPI backend, and presents filtered bed and breakfast search results.

---

**DEPENDENCIES**

- **Flask:** A Python web framework simplifying web application development.
- **Requests:** An HTTP library utilized for making requests to external APIs.

---

**CODE EXPLANATION**

- **Form Creation:** The SearchForm class instance manages user input through SelectFields for 'Air Conditioning' and 'Pets Allowed'.
- **Form Validation:** Upon form submission and validation, the input data constructs a URL for the FastAPI backend.
- **FastAPI Backend Request:** A GET request is sent to the FastAPI backend using the constructed URL. Exception handling generates error messages if issues arise.
- **Data Parsing:** Upon successful request completion, JSON data from the FastAPI response is parsed.
- **Rendering:** The retrieved data, along with the form and potential error messages, is rendered using the "search.html" template.

---

**USAGE**

To integrate the frontend with the backend for filtered bed and breakfast searches:

1. **Ensure Flask Backend Accessibility:** Verify the operational status and accessibility of the Flask backend.

2. **Update FastAPI Backend URL:** Modify the `FASTAPI_BACKEND_HOST` variable to correspond with the appropriate FastAPI backend URL.

3. **Implement Frontend Code:** Integrate the provided frontend code into your web application.

4. **Develop HTML Template:** Create an HTML template (e.g., "search.html") to showcase the search form and display the filtered results.

5. **Customize Form Fields and Design:** Tailor the form fields and design elements to align with your application's specific requirements and visual aesthetics.

