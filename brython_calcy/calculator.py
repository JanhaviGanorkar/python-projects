from browser import document, alert

def calculate(event):
    # Get input values
    num1 = float(document["num1"].value)
    num2 = float(document["num2"].value)
    operation = document["operation"].value
    result = None

    # Perform the calculation
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"

    # Update the result in the DOM
    document["result"].text = str(result)

# Attach event listener to the button
document["calculate"].bind("click", calculate)
