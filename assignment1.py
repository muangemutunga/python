num1 = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))


if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"{num1} {operation} {num2} = {result}")
