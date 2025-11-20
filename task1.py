# Create a Python function called "process_data" that accepts a list of mixed data types (numbers, strings, others) as input and performs the following steps:
#
# 1. Function and data types: The function should accept a list (data type list) and return a floating point number (data type float) as the overall result.
# 2. Control structure (iteration): Loop through the entire input list with a for loop.
# 3. Control structures (conditions):
#   - If an element is an integer (int) or a floating-point number (float), add it directly to a running total.
#   - If an element is a string (str), try to convert it to a number.
# 4. Error handling:
#   - Use a try...except block to attempt to convert the string.
#   - If the conversion is successful (e.g., for "15.5" or "10"), add the numeric value to the sum.
#   - If the conversion fails (e.g., for "Hello" or "Error"), output a message to the console stating that the string element was ignored.
# 5. Handling other types: If an element has a different type (e.g., bool, NoneType), output an appropriate message and ignore the element for the sum.

# Test Data:
# test_data = [
#     42,
#     10.5,
#     "20",
#     "3.14159",
#     "Das ist keine Zahl",
#     -5,
#     True,
#     None,
#     "7.0"
# ]

# this function does something
def process_data(datalist):
    
    total_sum = 0.0
    
    # Iteration
    for element in datalist:
        if isinstance(element, (int, float)):
            total_sum += element
            print(f"Number found: {element} -> Sum: {total_sum}")
        elif isinstance(element, str):
            #try - except and convert it into a number
            try:
                number_from_string = float(element)
                total_sum += number_from_string
                print(f"String converted and added: '{element}' -> Sum: {total_sum}")
            except ValueError:
                # Error case: String is not a valid number
                print(f"ERROR: String '{element}' could not be converted to a number and is ignored")
                
        else:
            # Ohter types
            print(f"Unknown data type ({type(element).__name__}) for element '{element}' will be ignored")
    
    return total_sum

# Test Data:
test_data = [
    42,
    10.5,
    "20",
    "3.14159",
    "Das ist keine Zahl",
    -5,
    True,
    None,
    "7.0"
]

# Execution
end_result = process_data(test_data)
print("\n--- RESULT ---")
print(f"The total amount is: {end_result}")





















# def process_data(datalist: list) -> float:
#     """
#     Processes a list of mixed data types, sums numeric values, 
#     and handles string conversion errors.
#     """
#     total_sum: float = 0.0
    
#     # 1Control structure: Iteration through the list
#     for element in datalist:
#         # 2. Control structure: Conditional processing by type
#         if isinstance(element, (int, float)):
#             # Case 1: Already a number (int or float)
#             total_sum += element
#             print(f"Number found: {element} -> Sum: {total_sum}")
            
#         elif isinstance(element, str):
#             # Case 2: String - Attempt to convert (with error handling)
#             # 3. Error handling: try-except block
#             try:
#                 # Attempts to convert the string to a float
#                 number_from_string = float(element)
#                 total_sum += number_from_string
#                 print(f"String converted and added: '{element}' -> Sum: {total_sum}")
                
#             except ValueError:
#                 # Error case: String is not a valid number
#                 print(f"ERROR: String '{element}' could not be converted to a number and is ignored.")
                
#         else:
#             # Case 3: Other data types
#             print(f"Unknown data type ({type(element).__name__}) for element '{element}' will be ignored.")
            
#     # Returning the result
#     return total_sum

# # test data
# test_data = [
#     42,
#     10.5,
#     "20",
#     "3.14159",
#     "Das ist keine Zahl",
#     -5,
#     True, # True is treated as 1 because it is a subtype of int.
#     None,
#     "7.0"
# ]

# # Execution of the function and output of the final result
# end_result = process_data(test_data)
# print("\n--- Result ---")
# print(f"The final total amount is: {end_result}")