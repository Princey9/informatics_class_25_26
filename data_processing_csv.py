# Create a Python function named process_inventory_data that reads product 
# data from a CSV file, performs a calculation, and then writes the results to a new JSON file.
# 1. Function and Data Types
# The main function process_inventory_data should accept two string arguments:
#     - csv_filepath: The path to the input CSV file.
#     - json_filepath: The path for the output JSON file.
# The function should return a Boolean (True if processing and writing were successful, False otherwise).
# 2. Input Data (CSV)
# The input CSV file contains product inventory data with the following structure:
#     product_id  name      unit_price    stock 
#     P001        Laptop    1200.50       15
#     P002        Mouse     25.00         200
#     P003        Keyboard  75.99         0
#     P004        Monitor   350.75        40
#     P005        Charger   N/A           50
# 3. Data Processing (Control Structures & Handling)
# Inside the function, perform the following steps:
#     - Reading (CSV): Read the data from the CSV file.
#     - Iteration & Calculation: Iterate through each row and calculate the total_value for each 
#     product using the formula:
#         total_value = unit_price x stock
#     - Error Handling: Use try...except blocks to handle potential errors:
#         - File Errors: Handle FileNotFoundError when reading the CSV.
#         - Data Conversion Errors: Safely convert unit_price and stock columns to appropriate 
#         numeric types (float and int). If the conversion fails 
#         (e.g., due to "N/A" or an empty string), treat the affected value as zero (0) and continue processing.
        
# 4. Output Data (JSON)
# Write the processed data as a list of dictionaries to the specified JSON file. 
# Each dictionary in the output should contain the original fields plus the calculated total_value.

import csv
import json
import os
from typing import List, Dict, Any

def process_inventory_data(csv_filepath, json_filepath):
    
    processed_data: List[Dict[str, Any]] = []
    # Reads inventory data form CSV
    try:
        with open(csv_filepath, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # iterate through each row
            for row in reader:
                try:
                    unit_price = float(row.get('unit_price',0))
                except (ValueError, TypeError):
                    unit_price = 0.0
                
                try:
                    stock = int(row.get('stock', 0))
                except (ValueError, TypeError):
                    stock = 0
                    
                # Calculation
                total_value = round(unit_price * stock, 2)
                
                # Create dictionary for JSON file entry
                processed_row = {
                    'product_id': row.get('product_id'),
                    'name': row.get('name'),
                    'unit_prict': unit_price,
                    'stock': stock,
                    'total_value': total_value
                }
                processed_data.append(processed_row)
            
    except FileNotFoundError:
        print(f"ERROR: Input CSV file not found at {csv_filepath}")
        return False
    except Exception as e:
        print(f"There is an unexpected error named {e}")
        return False
    
    # Writing to JSON File
    try:
        with open(json_filepath, mode='w', encoding='utf-8') as jsonfile:
            json.dump(processed_data, jsonfile, indent=4)
        return True
    except Exception as e:
        print(f"ERROR: could not write output to JSON: {e}")
        return False


INPUT_FILENAME = "test_csv_data_1.csv"
OUTPUT_FILENAME = "processed_data.json"

csv_filepath = os.path.join(INPUT_FILENAME)
json_filepath = os.path.join(OUTPUT_FILENAME)

process_inventory_data(csv_filepath, json_filepath)


























# import csv
# import json
# import os
# import unittest
# from typing import List, Dict, Any

# # --- Main Function ---

# def process_inventory_data(csv_filepath: str, json_filepath: str) -> bool:
#     """
#     Reads inventory data from CSV, calculates total value, and writes results to JSON.
#     """
#     processed_data: List[Dict[str, Any]] = []

#     # 1. Reading and File Error Handling
#     try:
#         with open(csv_filepath, mode='r', newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile)
            
#             # 2. Iteration and Calculation
#             for row in reader:
#                 try:
#                     # Safely convert unit_price to float (or 0 if error)
#                     unit_price = float(row.get('unit_price', 0))
#                 except (ValueError, TypeError):
#                     unit_price = 0.0
                
#                 try:
#                     # Safely convert stock to int (or 0 if error)
#                     stock = int(row.get('stock', 0))
#                 except (ValueError, TypeError):
#                     stock = 0
                
#                 # Calculation
#                 total_value = round(unit_price * stock, 2)
                
#                 # Create the processed dictionary
#                 processed_row = {
#                     'product_id': row.get('product_id'),
#                     'name': row.get('name'),
#                     'unit_price': unit_price,
#                     'stock': stock,
#                     'total_value': total_value
#                 }
#                 processed_data.append(processed_row)
                
#     except FileNotFoundError:
#         print(f"ERROR: Input CSV file not found at {csv_filepath}")
#         return False
#     except Exception as e:
#         print(f"An unexpected error occurred during CSV reading: {e}")
#         return False

#     # 3. Writing (JSON)
#     try:
#         with open(json_filepath, mode='w', encoding='utf-8') as jsonfile:
#             json.dump(processed_data, jsonfile, indent=4)
#         return True
#     except Exception as e:
#         print(f"ERROR: Could not write output JSON file: {e}")
#         return False



# #INPUT_FOLDER = "/Pfad/zu/Ihrem/Datenordner"  # Beispiel: "C:/Users/IhrName/Desktop/Daten" oder "/home/user/data"
# INPUT_FILENAME = "test_csv_data_1.csv"
# OUTPUT_FILENAME = "processed_inventory_results.json"

# # csv_filepath = os.path.join(INPUT_FOLDER, INPUT_FILENAME)
# # json_filepath = os.path.join(INPUT_FOLDER, OUTPUT_FILENAME)
# csv_filepath = os.path.join(INPUT_FILENAME)
# json_filepath = os.path.join(OUTPUT_FILENAME)

# # create an example data if no file exists
# # if not os.path.exists(INPUT_FOLDER):
# #         os.makedirs(INPUT_FOLDER)
# #         print(f"Ordner '{INPUT_FOLDER}' erstellt.")
        
# if not os.path.exists(csv_filepath):
#     print(f"Erstelle Beispieldatei {INPUT_FILENAME}...")
#     sample_data = [
#         ['product_id', 'name', 'unit_price', 'stock'],
#         ['P001', 'Laptop', '1200.50', '15'],
#         ['P003', 'Keyboard', '75.99', '0'],
#         ['P005', 'Charger', 'N/A', '50']  # Fehlerhafter Wert für Test
#     ]
#     with open(csv_filepath, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerows(sample_data)
    
# # Führen Sie die Hauptfunktion aus
# process_inventory_data(csv_filepath, json_filepath)



# # --- Unit Tests ---

# class TestDataProcessor(unittest.TestCase):
    
#     # Define file names
#     TEST_CSV_FILE = 'test_inventory.csv'
#     TEST_JSON_FILE = 'processed_output.json'

#     # Set up method to create a clean test environment (runs before each test)
#     def setUp(self):
#         # Create a mock CSV file for testing
#         csv_data = [
#             ['product_id', 'name', 'unit_price', 'stock'],
#             ['P101', 'Book', '15.00', '100'],
#             ['P102', 'Pen', '2.50', '200'],
#             ['P103', 'Ruler', 'N/A', '50'],            # Invalid unit_price
#             ['P104', 'Eraser', '1.00', 'out_of_stock'], # Invalid stock
#             ['P105', 'Laptop', '1200.00', '5'],
#         ]
#         with open(self.TEST_CSV_FILE, 'w', newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             writer.writerows(csv_data)

#     # Clean up method (runs after each test)
#     def tearDown(self):
#         # Delete test files if they exist
#         if os.path.exists(self.TEST_CSV_FILE):
#             os.remove(self.TEST_CSV_FILE)
#         if os.path.exists(self.TEST_JSON_FILE):
#             os.remove(self.TEST_JSON_FILE)

#     # --- Test Cases ---

#     def test_successful_processing(self):
#         # 1. Execute the function
#         result = process_inventory_data(self.TEST_CSV_FILE, self.TEST_JSON_FILE)
        
#         # 2. Check if the function returned True (Success)
#         self.assertTrue(result, "Function should return True on success")
        
#         # 3. Check if the output JSON file was created
#         self.assertTrue(os.path.exists(self.TEST_JSON_FILE), "Output JSON file should be created")
        
#         # 4. Read and validate the content
#         with open(self.TEST_JSON_FILE, 'r', encoding='utf-8') as f:
#             data = json.load(f)
        
#         self.assertEqual(len(data), 5, "Should process all 5 rows")
        
#         # Check an expected row (P101: 15.00 * 100 = 1500.00)
#         self.assertEqual(data[0]['product_id'], 'P101')
#         self.assertEqual(data[0]['total_value'], 1500.0)
        
#         # Check a row with successful error handling (P103: 'N/A' price treated as 0 * 50 = 0)
#         self.assertEqual(data[2]['name'], 'Ruler')
#         self.assertEqual(data[2]['unit_price'], 0.0) # Check price handling
#         self.assertEqual(data[2]['total_value'], 0.0)
        
#         # Check a row with successful error handling (P104: 'out_of_stock' stock treated as 0)
#         self.assertEqual(data[3]['name'], 'Eraser')
#         self.assertEqual(data[3]['stock'], 0) # Check stock handling
#         self.assertEqual(data[3]['total_value'], 0.0)
        
#         # Check the last row (P105: 1200.00 * 5 = 6000.00)
#         self.assertEqual(data[4]['total_value'], 6000.0)

#     def test_file_not_found_error(self):
#         # Test case where the input CSV file does not exist
#         result = process_inventory_data('non_existent.csv', self.TEST_JSON_FILE)
#         self.assertFalse(result, "Should return False if input file is not found")
#         self.assertFalse(os.path.exists(self.TEST_JSON_FILE), "Output file should not be created on read error")

# # Run the tests if the script is executed directly
# if __name__ == '__main__':
#     # Set argv to just the script name to prevent unittest from trying to use command-line arguments
#     import sys
#     sys.argv = [sys.argv[0]] 
#     unittest.main()