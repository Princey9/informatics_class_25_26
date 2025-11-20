# Create a Python function named update_inventory_excel that reads an Excel file (.xlsx), 
# performs a new calculation, and saves the updated data into a new Excel file. 
# This task focuses on utilizing the pandas library for robust data manipulation 
# and openpyxl for read/write Excel.
# Check on https://pypi.org/ for these libraries.
# Be aware that it could be to update your pip by "python.exe -m pip install --upgrade pip"

# 1. Function and Preparation
# The function should accept two string paths:
#     - input_filepath: Path to the source file.
#     - output_filepath: Path to the destination file.

# 2. Data Processing (with pandas)
# After loading the data into a pandas.DataFrame, perform the following steps:
#     - Add New Column: Add a new column named reorder_needed. This column should 
#     contain the boolean value True if the stock is less than 10, otherwise False.
#     - Data Cleaning: Fill all missing values (e.g., NaN or empty cells) in the 
#     comment column with the string "No comment".
#     - Type Handling (Best Practice): Use pd.to_numeric to ensure the stock column 
#     is correctly handled as a numeric type before the reorder check, gracefully 
#     handling any non-numeric entries.

# 3. Saving
# Save the modified DataFrame to a new Excel file at the specified output_filepath.



































# import pandas as pd
# import os

# # --- Path Configuration ---
# INPUT_FILE = "input_inventory.xlsx"
# OUTPUT_FILE = "updated_inventory.xlsx"

# # Create temporary paths for the example
# input_filepath = INPUT_FILE
# output_filepath = OUTPUT_FILE
# # -----------------------------------


# def create_sample_excel(filepath: str):
#     """Creates a sample Excel file for the exercise."""
#     data = {
#         'product_id': ['P101', 'P102', 'P103', 'P104', 'P105'],
#         'name': ['Monitor', 'Headset', 'Webcam', 'Microphone', 'Router'],
#         'unit_price': [350.50, 45.99, 120.00, 80.00, 200.00],
#         'stock': [25, 5, 8, 15, 2],
#         'comment': ['Newly arrived', None, 'Check order', 'Good sales', None]
#     }
#     df = pd.DataFrame(data)
#     df.to_excel(filepath, index=False)
#     print(f"INFO: Sample file '{filepath}' successfully created.")


# def update_inventory_excel(input_filepath: str, output_filepath: str) -> bool:
#     """
#     Reads an Excel file, adds a 'reorder_needed' column, and saves the updated data.
#     """
    
#     # 1. Reading the Excel file (with error handling)
#     try:
#         # Reads the first sheet by default
#         df = pd.read_excel(input_filepath)
#         print(f"INFO: {input_filepath} successfully read. Rows: {len(df)}")
#     except FileNotFoundError:
#         print(f"ERROR: Input file not found: {input_filepath}")
#         return False
#     except Exception as e:
#         print(f"ERROR: Error reading Excel file: {e}")
#         return False

#     # 2. Data Cleaning
#     print("INFO: Performing data cleaning...")
#     try:
#         # Replace NaN values in the 'comment' column with "No comment"
#         df['comment'] = df['comment'].fillna("No comment")
#     except KeyError:
#         print("WARNING: Column 'comment' not found, skipping cleaning.")
    
#     # 3. Add New Column and Calculation (Control Structure / Vectorization)
#     print("INFO: Adding 'reorder_needed' column...")
    
#     try:
#         # Ensure the 'stock' column is numeric. 'errors=coerce' converts non-numeric values to NaN.
#         df['stock'] = pd.to_numeric(df['stock'], errors='coerce')
        
#         # Vectorized Logic: True if stock < 10, otherwise False
#         df['reorder_needed'] = df['stock'] < 10
        
#     except KeyError:
#         print("ERROR: Column 'stock' not found. Calculation skipped.")
#         return False

#     # 4. Saving to a new Excel file (with error handling)
#     try:
#         # Save the DataFrame to a new Excel file (index=False removes the pandas index column)
#         df.to_excel(output_filepath, index=False)
#         print(f"\nSUCCESS: Updated data saved to: {output_filepath}")
#         print("The new 'reorder_needed' column has been added.")
#         return True
#     except Exception as e:
#         print(f"ERROR: Error saving the Excel file: {e}")
#         return False

# # --- Main Code Execution ---
# # if __name__ == '__main__':
# #     # 1. Create the source file
# #     create_sample_excel(input_filepath)

# #     # 2. Execute the main function
# #     update_inventory_excel(input_filepath, output_filepath)
    
# #     # Optional: Clean up temporary files (uncomment for real application cleanup)
# #     # os.remove(INPUT_FILE)
# #     # os.remove(OUTPUT_FILE)
    
    
# import unittest

# # WICHTIG: Die Funktionen update_inventory_excel und create_sample_excel
# # müssen im selben Skript definiert sein, damit die Tests funktionieren.

# class TestExcelInventoryUpdate(unittest.TestCase):
#     """
#     Testklasse für die Funktion update_inventory_excel.
#     """
    
#     # Definierte Dateinamen für die Tests
#     TEST_INPUT_FILE = 'test_input_inventory.xlsx'
#     TEST_OUTPUT_FILE = 'test_updated_inventory.xlsx'
    
#     # --- Setup und Teardown für saubere Testumgebung ---

#     def setUp(self):
#         """Wird vor jedem Testlauf ausgeführt. Erstellt die Beispieldatei."""
#         # Daten, die speziell für diesen Test verwendet werden
#         test_data = {
#             'product_id': ['A01', 'A02', 'A03', 'A04', 'A05'],
#             'name': ['Item A', 'Item B', 'Item C', 'Item D', 'Item E'],
#             'unit_price': [10.0, 50.0, 100.0, 1.0, 7.5],
#             'stock': [20, 5, 9, 10, 1], # 5, 9, 1 sind < 10 (True erwartet)
#             'comment': ['OK', None, 'Defekt', 'NaN', None]
#         }
#         df = pd.DataFrame(test_data)
#         df.to_excel(self.TEST_INPUT_FILE, index=False)

#     def tearDown(self):
#         """Wird nach jedem Testlauf ausgeführt. Löscht alle erstellten Dateien."""
#         if os.path.exists(self.TEST_INPUT_FILE):
#             os.remove(self.TEST_INPUT_FILE)
#         if os.path.exists(self.TEST_OUTPUT_FILE):
#             os.remove(self.TEST_OUTPUT_FILE)

#     # --- Testfälle ---

#     def test_successful_run_and_output_file_creation(self):
#         """Testet, ob die Funktion True zurückgibt und die Ausgabedatei erstellt wird."""
        
#         # 1. Funktion ausführen
#         result = update_inventory_excel(self.TEST_INPUT_FILE, self.TEST_OUTPUT_FILE)
        
#         # 2. Assertions
#         self.assertTrue(result, "Die Funktion sollte True zurückgeben.")
#         self.assertTrue(os.path.exists(self.TEST_OUTPUT_FILE), "Die Ausgabedatei sollte existieren.")

#     def test_calculation_and_data_cleaning(self):
#         """Testet die Logik der Berechnung und die Datenbereinigung."""
        
#         # 1. Funktion ausführen
#         update_inventory_excel(self.TEST_INPUT_FILE, self.TEST_OUTPUT_FILE)
        
#         # 2. Ergebnisdatei einlesen
#         df_result = pd.read_excel(self.TEST_OUTPUT_FILE)
        
#         # 3. Assertions für die Berechnung ('reorder_needed' Spalte)
        
#         # Erwartete Werte: Stock: [20, 5, 9, 10, 1] -> Expected Reorder: [False, True, True, False, True]
#         expected_reorder = [False, True, True, False, True]
        
#         # Überprüfe, ob die 'reorder_needed' Spalte existiert
#         self.assertIn('reorder_needed', df_result.columns, "Die Spalte 'reorder_needed' fehlt.")
        
#         # Überprüfe die berechneten Werte zeilenweise
#         self.assertListEqual(df_result['reorder_needed'].tolist(), expected_reorder, 
#                              "Die Berechnung der 'reorder_needed'-Spalte ist falsch.")

#         # 4. Assertions für die Datenbereinigung ('comment' Spalte)
        
#         # Überprüfe, ob None-Werte durch "No comment" ersetzt wurden
#         # Original: ['OK', None, 'Defekt', 'NaN', None]
#         expected_comments = ['OK', 'No comment', 'Defekt', 'No comment', 'No comment']
        
#         # pandas.read_excel konvertiert leere Zellen zu NaN, welches dann in der Funktion zu "No comment" wird.
#         # Strings wie 'NaN' im Original-Input bleiben unverändert, aber die fehlenden Werte werden gefüllt.
#         # NOTE: Bei der Verwendung von 'NaN' als String in der Input-Daten (wie hier im setup) 
#         # muss man vorsichtig sein, da es nicht automatisch als fehlender Wert erkannt wird. 
#         # Hier gehen wir davon aus, dass nur die echten None/NaN-Werte (Index 1 und 4) gefüllt werden.
        
#         # Überprüfe die gefüllten Werte (Index 1 und 4 waren None)
#         self.assertEqual(df_result.loc[1, 'comment'], 'No comment', "Fehlender Wert (Index 1) wurde nicht gefüllt.")
#         self.assertEqual(df_result.loc[4, 'comment'], 'No comment', "Fehlender Wert (Index 4) wurde nicht gefüllt.")


#     def test_file_not_found_error(self):
#         """Testet die Fehlerbehandlung, wenn die Eingabedatei fehlt."""
        
#         # Lösche die Eingabedatei explizit, falls sie im Setup erstellt wurde
#         if os.path.exists(self.TEST_INPUT_FILE):
#             os.remove(self.TEST_INPUT_FILE)
            
#         # 1. Funktion mit fehlendem Pfad ausführen
#         result = update_inventory_excel(self.TEST_INPUT_FILE, self.TEST_OUTPUT_FILE)
        
#         # 2. Assertions
#         self.assertFalse(result, "Sollte False zurückgeben, wenn die Datei nicht gefunden wird.")
#         self.assertFalse(os.path.exists(self.TEST_OUTPUT_FILE), "Es sollte keine Ausgabedatei erstellt werden.")


# # --- Ausführung der Tests ---

# if __name__ == '__main__':
#     # Führt alle Tests in der Testklasse aus
#     unittest.main()