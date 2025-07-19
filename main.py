History_file = 'history.txt'

def history_show():
    try:
        with open(History_file, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No History Found")
            else:
                print("Calculation History:")
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No History Found")

def delete_history():
    open(History_file, 'w').close()
    print("History Cleared!")

def save_history(user_input, result):
    with open(History_file, 'a') as file:
        file.write(f"{user_input} = {result}\n")

        
def calculator(user_input):
    # Detect operator and split manually
    for op in ['+', '-', '*', '/']:
        if op in user_input:
            parts = user_input.partition(op)
            break
    else:
        print("Invalid Input! Please enter like (e.g. 1+2)")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers.")
        return

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("It cannot be divided by 0")
            return
        result = num1 / num2
    else:
        print("Invalid operator! Use one of (+, -, *, /)")
        return

    print(f"Result: {result}")
    save_history(user_input, result)

def main():
    print("Welcome to the calculator!")
    while True:
        user_input = input("Enter expression or 'history', 'clear', 'exit': ").lower()
        if user_input == 'exit':
            print("GOODBYE")
            break
        elif user_input == 'history':
            history_show()
        elif user_input == 'clear':
            delete_history()
        else:
            calculator(user_input)

main()
