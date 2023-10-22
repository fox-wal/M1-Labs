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

    is_correct = False
    TRIES = 3

    for i in range(TRIES):
        # Get input
        user_answer = int(input("Enter the correct answer: "))

        is_correct = user_answer == correct_answer

        if is_correct:
            print("Correct")
            break
        else:
            print("Incorrect")

    return is_correct

# Constants
NUM_OF_QUESTIONS = 3
OPERAND_1S = [ 30, 51, 24 ]
OPERAND_2S = [ 13, 20, 59 ]

# Start quiz
is_correct = False
correct_count = 0

for i in range(NUM_OF_QUESTIONS):
    is_correct = ask_question(OPERAND_1S[i], OPERAND_2S[i])
    if is_correct:
        correct_count += 1

# Output summary
print("You answered", correct_count, "out of", NUM_OF_QUESTIONS, "questions correctly.")