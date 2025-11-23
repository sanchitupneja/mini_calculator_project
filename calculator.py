# Simple Calculator
# Owner: Sanchit
# Roll No: 2501730475

def add(a,b): return a + b
def subtract(a,b): return a - b
def multiply(a,b): return a * b
def divide(a,b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    print("=== Calculator ===")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print("Result:", add(a,b))
    elif op == '-':
        print("Result:", subtract(a,b))
    elif op == '*':
        print("Result:", multiply(a,b))
    elif op == '/':
        print("Result:", divide(a,b))
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
