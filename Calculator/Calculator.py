"This program will print a calculator."


logo = '''
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|

'''
print(logo)
calculate = True

while calculate:
    num1 = float(input("What's the first number?: "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    num2 = float(input("What's the next number?: "))

    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    if operation == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == "-":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == "*":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == "/":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Wrong choice")

    continue_calculation = input("Type 'y' for new calculation and Type 'n' for existing the calculator: ")
    if continue_calculation == 'n':
        calculate = False
        print("Goodbye!")
