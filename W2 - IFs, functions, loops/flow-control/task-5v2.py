#
# QUIZ
#

def ask_question(operand_1, operand_2) -> bool:
    # Set up question and answers
    question = f"{operand_1} * {operand_2} = ?"
    correct_answer = operand_1 * operand_2
    answers = [
        correct_answer,
        correct_answer + operand_2,
        correct_answer - operand_1
        ]

    # Display question
    print(question)
    for a in answers:
        print(a)

    # Get input
    user_answer = int(input("Enter the correct answer: "))

    return user_answer == correct_answer

def print_result(is_correct: bool):
    if is_correct:
        print("Correct")
    else:
        print("Incorrect")

# Constants
NUM_OF_QUESTIONS = 3
OPERAND_1S = [ 30, 51, 24 ]
OPERAND_2S = [ 13, 20, 59 ]

# Start quiz
is_correct = False
correct_count = 0

for i in range(NUM_OF_QUESTIONS):
    is_correct = ask_question(OPERAND_1S[i], OPERAND_2S[i])
    print_result(is_correct)
    if is_correct:
        correct_count += 1

# Output summary
print("You answered", correct_count, "out of", NUM_OF_QUESTIONS, "questions correctly.")