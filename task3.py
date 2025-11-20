import unittest

# Create a Python function named process_data_from_json that takes a single argument expected to be a 
# data structure resembling parsed JSON data (a Python dictionary or list). 
# The goal is to safely extract and calculate the sum of specific numerical values within this structure.
# 1. Function and Data Types: The function should accept any data type as input and return an integer (int) 
# representing the calculated total.
# 2. Error Handling (Input Type): Use a try...except block to ensure the input data is a dictionary (dict).
#     If the input is not a dictionary (e.g., a list, a string, or None), catch the appropriate error, 
# print a brief message, and return 0.
# 3. Data Extraction (Control Structure): The function must attempt to extract three specific values 
# from the dictionary under the keys: "base_value", "multiplier", and "offset".
# 4. Error Handling (Key/Value): Use nested try...except blocks or a robust lookup pattern (like .get()) 
# to handle two scenarios:
#     - Missing Keys: If any of the required keys are missing, they should be treated as having a value of 0.
#     - Non-Numeric Values: If a key exists but its value is not an int or float (e.g., it's a string like "N/A")
# , treat that value as 0.
# 5. Calculation: The final result is calculated using the following formula:
#     Result = (base_value + offset) x multiplier

# Expected Calculation Example:
# If the input is {"base_value": 10, "multiplier": 5, "offset": 2}, the result should be (10 + 2) x 5 = 60.

def process_data_from_json(data_structure):
    
    if not isinstance(data_structure, dict):
        print(f"ERROR: expected dict input, got {type(data_structure).__name__}. Returning 0.")
        return 0
    
    keys_to_process = ["base_value", "multiplier", "offset"]
    
    base_value = 0
    multiplier = 0
    offset = 0
    
    for key in keys_to_process:
        try:
            value = data_structure[key]
        except KeyError:
            # Key is missing, treat as 0
            continue
        
        try:
            numeric_value = float(value)
        except (TypeError, ValueError):
            #print(f"Warning: non-numeric value found for key '{key}'")
            numeric_value = 0
            
        if key == "base_value":
            base_value = numeric_value
        elif key == "multiplier":
            multiplier = numeric_value
        elif key == "offset":
            offset = numeric_value
            
        result = (base_value + offset) * multiplier
    
    return int(round(result))

# data = {"base_value": 10, "multiplier": 5, "offset": 2}
# result = process_data_from_json(data)
# print(result)

class TestJsonProcessor(unittest.TestCase):
    
    def test_full_valid_data(self):
        data = {"base_value": 10, "multiplier": 5, "offset": 2}
        self.assertEqual(process_data_from_json(data), 60)

    def test_none_numeric_values(self):
        data = {"base_value": "ten", "multiplier": "five", "offset": "two"}
        self.assertEqual(process_data_from_json(data), 0)
        
    def test_mixed_values(self):
        data = {"base_value": 10, "multiplier": "five", "offset": 2}
        self.assertEqual(process_data_from_json(data), 0)
        
    def test_not_instance_of_string(self):
        data = {"base_value": "ten", "multiplier": "five", "offset": "two"}
        self.assertNotIsInstance(process_data_from_json(data), type("0"))

unittest.main()

















# import unittest

# def process_data_from_json(data_structure) -> int:
#     """
#     Safely extracts and calculates a result from a dictionary, handling 
#     missing keys and non-numeric values.
#     Result formula: (base_value + offset) * multiplier
#     """
#     if not isinstance(data_structure, dict):
#         # 1. Error Handling (Input Type)
#         print(f"Error: Expected dict input, got {type(data_structure).__name__}. Returning 0.")
#         return 0

#     base_value = 0
#     multiplier = 0
#     offset = 0

#     # List of keys to process
#     keys_to_process = ["base_value", "multiplier", "offset"]

#     for key in keys_to_process:
#         # 2. Control Structure (Key/Value Retrieval) & Error Handling (Missing Keys)
#         try:
#             value = data_structure[key]
#         except KeyError:
#             # Key is missing, treat as 0 (default values are already 0)
#             continue
        
#         # 3. Error Handling (Non-Numeric Values)
#         try:
#             # Attempt to convert to float first to handle strings like "10.5"
#             numeric_value = float(value)
#         except (TypeError, ValueError):
#             # Value is non-numeric (e.g., 'N/A', None, 'ten'), treat as 0
#             # print(f"Warning: Non-numeric value found for key '{key}'. Treated as 0.") # Optional feedback
#             numeric_value = 0
        
#         # 4. Assign the safely extracted numeric value
#         # Note: We round to int at the end of the calculation, but use float here for intermediate precision
#         if key == "base_value":
#             base_value = numeric_value
#         elif key == "multiplier":
#             multiplier = numeric_value
#         elif key == "offset":
#             offset = numeric_value
            
#     # 5. Calculation
#     result = (base_value + offset) * multiplier
    
#     # Return the result as an integer
#     return int(round(result))

# # -----------------------------------------------------------------

# # --- Unit Tests ---

# class TestJsonProcessor(unittest.TestCase):
#     """
#     Test class for the process_data_from_json function.
#     """

#     ## 1. Tests for successful calculation
#     def test_full_valid_data(self):
#         data = {"base_value": 10, "multiplier": 5, "offset": 2}
#         # Result: (10 + 2) * 5 = 60
#         self.assertEqual(process_data_from_json(data), 60)

#     def test_zero_values(self):
#         data = {"base_value": 0, "multiplier": 10, "offset": 0}
#         # Result: (0 + 0) * 10 = 0
#         self.assertEqual(process_data_from_json(data), 0)

#     def test_negative_values(self):
#         data = {"base_value": 20, "multiplier": -2, "offset": 5}
#         # Result: (20 + 5) * -2 = -50
#         self.assertEqual(process_data_from_json(data), -50)
        
#     def test_float_values(self):
#         data = {"base_value": 10.5, "multiplier": 2, "offset": 1.5}
#         # Result: (10.5 + 1.5) * 2 = 12 * 2 = 24
#         self.assertEqual(process_data_from_json(data), 24)
        
#     def test_string_numbers(self):
#         data = {"base_value": "10", "multiplier": "5", "offset": "2"}
#         # Result: (10 + 2) * 5 = 60
#         self.assertEqual(process_data_from_json(data), 60)

#     ## 2. Tests for Error Handling (Missing Keys - Should default to 0)
#     def test_missing_multiplier(self):
#         data = {"base_value": 10, "offset": 2}
#         # Result: (10 + 2) * 0 = 0
#         self.assertEqual(process_data_from_json(data), 0)

#     def test_missing_base_value(self):
#         data = {"multiplier": 5, "offset": 2}
#         # Result: (0 + 2) * 5 = 10
#         self.assertEqual(process_data_from_json(data), 10)

#     def test_empty_dict(self):
#         data = {}
#         # Result: (0 + 0) * 0 = 0
#         self.assertEqual(process_data_from_json(data), 0)

#     ## 3. Tests for Error Handling (Non-Numeric Values - Should treat as 0)
#     def test_non_numeric_multiplier(self):
#         data = {"base_value": 10, "multiplier": "N/A", "offset": 2}
#         # Multiplier is 0. Result: (10 + 2) * 0 = 0
#         self.assertEqual(process_data_from_json(data), 0)
        
#     def test_mixed_invalid_types(self):
#         data = {"base_value": True, "multiplier": "5", "offset": [1, 2]}
#         # base_value is 1.0, multiplier is 5.0, offset is 0. 
#         # Result: (1 + 0) * 5 = 5
#         self.assertEqual(process_data_from_json(data), 5)
        
#     ## 4. Tests for Error Handling (Incorrect Input Type - Should return 0)
#     def test_input_is_list(self):
#         # Should be caught by the initial type check
#         self.assertEqual(process_data_from_json([1, 2, 3]), 0)

#     def test_input_is_none(self):
#         # Should be caught by the initial type check
#         self.assertEqual(process_data_from_json(None), 0)

#     def test_input_is_string(self):
#         # Should be caught by the initial type check
#         self.assertEqual(process_data_from_json("some string"), 0)


# # Run the tests if the script is executed directly
# if __name__ == '__main__':
#     unittest.main()