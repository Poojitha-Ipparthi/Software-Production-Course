import os

HISTORY_FILE = "/history/history.txt"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def save_history(operation, a, b, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{a} {operation} {b} = {result}\n")
        file.flush()  

def show_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            print("\nCalculation History:")
            print(file.read())
    else:
        print("\nNo history found.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")

        choice = input("Select an option (1-6): ")
        
        if choice in ["1", "2", "3", "4"]:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            
            if choice == "1":
                result = add(a, b)
                operation = "+"
            elif choice == "2":
                result = subtract(a, b)
                operation = "-"
            elif choice == "3":
                result = multiply(a, b)
                operation = "*"
            elif choice == "4":
                result = divide(a, b)
                operation = "/"
            
            print(f"Result: {result}")
            save_history(operation, a, b, result)
        
        elif choice == "5":
            show_history()
        
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    calculator()
