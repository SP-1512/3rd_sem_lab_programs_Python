def safe_division(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"The result of {numerator} / {denominator} is: {result}")
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero! Attempted {numerator} / {denominator}")
    except TypeError:
        print("Error: Invalid input types. Please provide numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 # Example function calls
 safe_division(10, 2)        # Normal case
 safe_division(10, 0)        # ZeroDivisionError
 safe_division("10", 2)      # TypeError
 safe_division(10, "a")      # TypeError
