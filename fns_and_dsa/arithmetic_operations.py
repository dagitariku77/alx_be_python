# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """Performs basic arithmetic operations.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float: The result of the operation, or a string message if division by zero occurs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is not allowed."  # Or return float('inf') for infinity
        else:
            return num1 / num2
    else:
        return "Invalid operation."  # Handle invalid operations (optional, but good practice)