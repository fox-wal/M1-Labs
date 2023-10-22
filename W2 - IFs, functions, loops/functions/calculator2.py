from enum import Enum

OPERATORS = "+-x*/"

class PrimaryStates(Enum):
    NUMBER = 0
    OPERATOR = 1

class SecondaryStates(Enum):
    DIGIT = 0
    MINUS_SIGN = 1
    DECIMAL_POINT = 2
    NONE = 3

def get_valid_next_states(current_states: tuple, decimal_point_visited: bool) -> (list[PrimaryStates], list[SecondaryStates]):
    valid_primary_states = [PrimaryStates.NUMBER]
    valid_secondary_states = [SecondaryStates.DIGIT]

    if current_states[0] == PrimaryStates.OPERATOR:
        valid_secondary_states.append(SecondaryStates.MINUS_SIGN)
        decimal_point_visited = False
    else:
        valid_secondary_states = [SecondaryStates.DIGIT]
        if current_states[1] == SecondaryStates.DIGIT:
            if not decimal_point_visited:
                valid_secondary_states.append(SecondaryStates.DECIMAL_POINT)
            valid_primary_states.append(PrimaryStates.OPERATOR)

    return (valid_primary_states, valid_secondary_states)

def determine_current_states(current_char: str, current_status: tuple) -> tuple[int, int, bool]:
    """
    Determine the current `primary state` and `secondary state` based on the current states and character.
    :param current_char: the current character of the entered expression being checked
    :return: Updated `primary state`, `secondary state`, and `decimal point visited` variables.
    """
    primary_state = current_status[0]
    secondary_state = current_status[1]
    decimal_point_visited = current_status[2]

    if current_char.isnumeric():
        primary_state = PrimaryStates.NUMBER
        secondary_state = SecondaryStates.DIGIT
    elif current_char == '.':
        primary_state = PrimaryStates.NUMBER
        secondary_state = SecondaryStates.DECIMAL_POINT
        decimal_point_visited = True
    elif "+x*/".__contains__(current_char):
        primary_state = PrimaryStates.OPERATOR
    elif current_char == '-':
        if primary_state == PrimaryStates.NUMBER:
            primary_state = PrimaryStates.OPERATOR
        else:
            primary_state = PrimaryStates.NUMBER
            secondary_state = SecondaryStates.MINUS_SIGN
    return (primary_state, secondary_state, decimal_point_visited)

def check_new_states_valid(valid_states: tuple[list], current_states: tuple[int]) -> bool:
    return (valid_states[0].__contains__(current_states[0])
        and valid_states[1].__contains__(current_states[1]))

def check_expression_format(expression: str) -> (str, bool):
    if expression.__contains__("/0"):
        return ("Cannot divide by zero.", False)
        
    primary_state: PrimaryStates = PrimaryStates.OPERATOR
    secondary_state: SecondaryStates = SecondaryStates.DIGIT

    valid_states = []

    decimal_point_visited = False

    for i in expression:
        valid_states = list(get_valid_next_states((primary_state, secondary_state), decimal_point_visited))
        result = determine_current_states(i, (primary_state, secondary_state, decimal_point_visited))
        primary_state = result[0]
        secondary_state = result[1]
        decimal_point_visited = result[2]
        if not check_new_states_valid(valid_states, (primary_state, secondary_state)):
            return ("Invalid expression format.", False)

    return (expression, True)

def take_user_expression():

    valid = False

    while not valid:
        expression = input("Enter expression: ").replace(" ", "")

        result = check_expression_format(expression)
        valid = result[1]

        if not valid:
            print(result[0])

    return expression

def split_by_operator(expression: str) -> (list[str], list[float]):
    operators = []
    operands = []
    start_of_num = 0
    for i in range(len(expression)):
        if OPERATORS.__contains__(expression[i]):
            if (i != 0) and (not OPERATORS.__contains__(expression[i - 1])):
                operators.append(expression[i])
                operands.append(float(expression[start_of_num:i]))
                start_of_num = i + 1
    operands.append(float(expression[start_of_num:]))

    return (operators, operands)

def calculate(operators: list[str], operands: list[float]) -> float:
    for operator in "/x*+-":
        while operators.__contains__(operator):
            i = 0
            while (len(operands) > 1) and (i < len(operators)):
                if operators[i] == operator:
                    operators.pop(i)
                    match operator:
                        case "/":
                            operands[i] /= operands.pop(i + 1)
                        case "x" | "*":
                            operands[i] *= operands.pop(i + 1)
                        case "+":
                            operands[i] += operands.pop(i + 1)
                        case "-":
                            operands[i] -= operands.pop(i + 1)
                i += 1
    return operands[0]

#------------------#
# Start of program #
#------------------#

expression = take_user_expression()
(operators, operands) = split_by_operator(expression)
calculate(operators, operands)