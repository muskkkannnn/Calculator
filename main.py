#version 1
from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : div
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation: ")
calculation_function = operations[operation_symbol]

num2 = int(input("What's the second number?: "))

answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
