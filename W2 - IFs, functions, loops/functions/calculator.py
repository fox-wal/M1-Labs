def display_operation_menu():
    """
    Display menu of different methematical operations for the user to choose from.
    """
    print("Select an option:\n(1) Add\n(2) Subtract\n(3) Multiply\n(4) Divide")

def user_chooses_menu_option() -> int:
    MIN = 1
    MAX = 4
    while True:
        try:
            choice = int(input())
            if (MIN <= choice) and (choice <= MAX):
                return choice
        except ValueError:
            print("Please enter an integer between", MIN, "and", MAX)

def user_enters_a_number(can_be_zero: bool = True) -> float:
    while True:
        try:
            number = float(input())
            if can_be_zero or (number != 0):
                return number
            else:
                print("Number cannot be 0.")
        except ValueError:
            print("Please enter a real number.")

def add(a, b) -> float:
    return a + b

def subtract(a, b) -> float:
    return a - b

def multiply(a, b) -> float:
    return a * b

def divide(a, b) -> float:
    return a / b

#------#
# Main #
#------#

user_response = "yes"

while user_response.lower() == "yes":
    display_operation_menu()
    choice = user_chooses_menu_option()

    print("Enter a first operand:")
    number1 = user_enters_a_number()
    print("Enter a second operand:")
    user_chose_division = choice != 4
    number2 = user_enters_a_number(user_chose_division)

    result = None
    match choice:
        case 1:
            result = add(number1, number2)
        case 2:
            result = subtract(number1, number2)
        case 3:
            result = multiply(number1, number2)
        case 4:
            result = divide(number1, number2)

    print("Result:", result)

    user_response = input("\nWould you like to perform another operation? (yes/no)")