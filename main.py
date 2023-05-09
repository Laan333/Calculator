from logos.ascii_art import logo
def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def first_num():
    num1 = int(input("What the first number?: "))
    return num1


operations_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}


def start(user_answer=None, result=0):
    num1 = 0
    if user_answer is None:
        num1 = first_num()
    elif user_answer == "Y":
        num1 = result
    num2 = int(input("What the second number?: "))
    for oper in operations_dict:
        print(oper)
    symbol = input("Pick operation: ")
    calculation(num1, num2, symbol)


def calculation(num1, num2, symbol):
    if symbol in operations_dict.keys():
        operation = operations_dict[symbol]
        result = operation(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")
        user_choice = input(f"Type 'Y' to continue calculating with {result}, or type 'N' to exit: ")
        if user_choice == "Y":
            start(user_answer=user_choice, result=result)

def main():
    start()


if __name__=="__main__":
    print(logo)
    main()