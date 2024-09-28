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

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Choose an operation: ")

for symbol in operations:
    print(symbol)
