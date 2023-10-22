#
# QUIZ
#

# Constants
OPERAND_1 = 10
OPERAND_2 = 10
QUESTION = f"{OPERAND_1} * {OPERAND_2} = ?"
CORRECT_ANSWER = OPERAND_1 * OPERAND_2
ANSWERS = [
    CORRECT_ANSWER,
    OPERAND_1 * OPERAND_2 + 10
    ]

# Display question
print(QUESTION)
i = "A"
for a in range(ANSWERS):
    print(f"{i}: {a}")
    i = chr(i + 1)

# Get input
user_answer = int(input("Enter the correct answer: "))

# Display feedback
if user_answer == CORRECT_ANSWER:
    print("Correct")
else:
    print("Incorrect")