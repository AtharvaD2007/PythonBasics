def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Invalid operation"

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

print("Result:", calculator(x, y, op))