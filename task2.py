# Create a Python function named validate_password that takes a single argument 
# (the password) and checks its strength.
# 1. Function and Data Types: The function should accept any data type as input 
# (although only strings are valid) and return a Boolean value (True or False).
# 2. Error Handling (Type Checking): Use an outer try...except block to ensure that 
# the input is actually a String (str).
#   If the input is not a string (e.g., a number, a list, or None), catch the error, 
# print an error message, and immediately return False.
# 3. Control Structure (Condition): Check the following criterion for password strength:
#   Length: The password must be at least 10 characters long. If it is not, 
# print a corresponding message and return False.
# 4. Control Structures (Iteration & Conditions): Use a for loop to iterate through 
# the password character by character and check if it contains at least the following:
#   - One uppercase letter.
#   - One lowercase letter.
#   - One digit (0-9).
# If all criteria are met, return True.

# Test calls:
# validate_password("abcD123")           # Too short, False
# validate_password("SuperPasswordWithoutNumber") # No digit, False
# validate_password("HelloWorld123")    # All criteria met, True
# validate_password(1234567890123)       # Incorrect data type, False


































def validate_password(password_input) -> bool:
    """
    Checks a password for minimum length, uppercase/lowercase letters, and digits.
    Uses error handling to catch non-string inputs.
    """
    # 1. Error Handling (Type Checking): try-except block
    try:
        # Attempt to call string-specific methods. 
        # If password_input is not a string, a TypeError will be raised here.
        password_length = len(password_input)
    except TypeError:
        print(f"ERROR: The input must be a string, but a {type(password_input).__name__} was passed.")
        return False
    
    # 2. Control Structure (Condition): Check length
    MIN_LENGTH = 10
    if password_length < MIN_LENGTH:
        print(f"Validation failed: Password is too short ({password_length} characters, at least {MIN_LENGTH} required).")
        return False
    
    # Initialize flags (boolean data type)
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    # 3. Control Structures (Iteration & Conditions): Check characters
    for char in password_input:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
            
        # Optional: Early exit once all criteria are met (performance optimization)
        if has_uppercase and has_lowercase and has_digit:
            break
            
    # 4. Control Structures (Conditions): Check final result
    if not has_uppercase:
        print("Validation failed: Missing at least one uppercase letter.")
    elif not has_lowercase:
        print("Validation failed: Missing at least one lowercase letter.")
    elif not has_digit:
        print("Validation failed: Missing at least one digit.")
    else:
        print("Validation successful: The password meets all strength requirements.")
        return True
        
    # If any of the final checks fail, False is returned
    return False

# --- Test the Function ---
print("--- Test 1: Too short ---")
print(f"Result: {validate_password('abcD123')}\n")

print("--- Test 2: No digit ---")
print(f"Result: {validate_password('SuperPasswordWithoutNumber')}\n")

print("--- Test 3: Valid ---")
print(f"Result: {validate_password('HelloWorld123')}\n")

print("--- Test 4: Incorrect Type (Number) ---")
print(f"Result: {validate_password(1234567890123)}\n")

print("--- Test 5: Incorrect Type (None) ---")
print(f"Result: {validate_password(None)}\n")