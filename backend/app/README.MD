**INTRODUCTION - FEATURE: "BED AND BREAKFAST FILTER"**

The FastAPI-based project enables the filtering of bed and breakfast (B&B) establishments based on specified amenities. Users can select accommodation based on criteria like air conditioning and pet allowances. The primary function, "essential_services_periphery," filters B&B structures using user-provided amenities and returns relevant information about these establishments.

The project relies on the following Python libraries:
- FastAPI: A fast, modern web framework for building APIs
- TestClient(FastAPI): A testing utility provided by FastAPI for simulating HTTP requests
- Pandas: A powerful library for data manipulation
---

**BACKEND DESCRIPTION**

The application employs FastAPI with CORS middleware for handling cross-origin requests. Using FastAPI's Query functionality, string values are parsed into boolean for amenities such as air conditioning and pet allowances. Data regarding B&B establishments is read from a CSV file ("dove-alloggiare.csv") and transformed into a Pandas DataFrame. Filtering is executed based on user-selected amenities through Pandas DataFrame operations.

---

**TESTS SUMMARY**

The test suite has been categorized into macro groups to ensure a comprehensive validation of the filtering functionality:

**1. Valid Inputs and Individual Parameter Testing:**
   - `test_air_conditioning_true`
   - `test_pets_allowed_true`
   - `test_both_true`
   - `test_both_false`
   - `test_air_conditioning_true_pets_false`
   - `test_air_conditioning_false_pets_true`

**2. Invalid Inputs and Parameter Combinations:**
   - `test_invalid_input`
   - `test_invalid_air_conditioning_param`
   - `test_invalid_pets_allowed_param`
   - `test_combination_invalid_params`
   - `test_combination_valid_and_invalid_params`
   - `test_invalid_air_conditioning_param_and_no_pets_allowed`
   - `test_valid_air_conditioning_param_and_invalid_pets_allowed`
   - `test_large_query_params`
   - `test_large_query_params_pets_allowed_true`

**3. Edge Cases and Absence of Parameters:**
   - `test_no_query_params`
   - `test_all_false`
   - `test_no_air_conditioning_param_and_valid_pets_allowed`
   - `test_no_pets_allowed_param_and_valid_air_conditioning`

**4. Miscellaneous and Endpoint Validation:**
   - `test_invalid_endpoint`
   - `test_both_true_pets_true`
   - `test_both_true_pets_false`
   - `test_both_false_pets_true`

---

**USAGE**

To utilize this functionality, follow these steps:
1. Ensure that the CSV file ("dove-alloggiare.csv") is located in the specified path in the code.
2. Access the "/essential_services_periphery" endpoint, providing appropriate query parameters for amenity-based filtering.
3. Utilize the provided unit tests to verify the correct functioning of the filtering feature across various scenarios.