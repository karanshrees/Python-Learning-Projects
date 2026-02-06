first_number = float(input("Enter a first number: "))
operation = input("Enter an operation (+, -, *, /): ")
second_number = float(input("Enter a second number: "))

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Error: Division by zero is not allowed."

print("Result:", result)