def perform_operation(num1, num2, operation):
    """"
    Perform basic airthemtic operations.
    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform: 'add', 'subtract', 'multiply' or 'divide'.

    Returns:
        float or str: The result of the operation, or an error message if invalid.
    """
    if operation =="add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
