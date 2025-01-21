# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division, handling errors like division by zero and non-numeric input."""
    try:
        # Attempt to convert both arguments to floats and perform the division
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle division by zero error
        return "Error: Cannot divide by zero."
    except ValueError:
        # Handle non-numeric input error
        return "Error: Please enter numeric values only."
