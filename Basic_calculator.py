def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return (a // b)


def power(a, b):
    return pow(a, b)


a = eval(input("First Number:\n"))
operation = (input("Enter the operation:\n "))
b = eval(input("Second Number:\n"))
if operation == '+':
    print(add(a, b))

elif operation == '-':
    print(sub(a, b))
elif operation == '*':
    print(mul(a, b))
elif operation == '/':
    print(div(a, b))
elif operation == '**':
    print(power(a, b))
