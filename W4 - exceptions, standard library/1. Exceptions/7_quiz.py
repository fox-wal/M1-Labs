#
# QUIZ
#

import datetime

QUESTION_NAME = 0
QUESTION = 1
ANSWERS = 2
CORRECT_ANSWER = 3
NUMBER_OF_ANSWER_OPTIONS = 4

def abend(message: str):
    """
    Abnormal termination sequence.
    :param message: The error message to display before exiting the program.
    """
    print("Error:", message)
    print("Press enter to exit.")
    input()
    exit()

def load_questions() -> list:
    """
    Load questions from file.
    :return: list of questions.
    """ 
    QUESTION_FILE = "quiz.txt"

    questions = []

    # Open file
    try:
        question_file = open(QUESTION_FILE, "r+")
    except OSError:
        raise OSError("Unable to open file.")

    # Load questions
    question_name: str
    question: str
    answers: list[str] = []
    correct_answer: str

    current_field = 0
    try:
        for line in question_file.readlines():
            line = line.removesuffix("\n")
            if (line is not None) and (line.__len__() != 0):

                # Question name
                if current_field == QUESTION_NAME:
                    question_name = line

                # Question
                elif current_field == QUESTION:
                    question = line

                # Answer options
                elif current_field < (ANSWERS + NUMBER_OF_ANSWER_OPTIONS):
                    if current_field == ANSWERS:
                        answers = []
                    answers.append(line)

                # Correct answer
                else:
                    correct_answer = line.split(':')[-1]

                current_field += 1

            # Next question
            else:
                questions.append([question_name, question, answers, correct_answer])
                current_field = 0
        
        questions.append([question_name, question, answers, correct_answer])
    except:
        raise OSError("Question file formatted incorrectly.")
    finally:
        question_file.close()

    return questions

def print_question(question: list):
    """
    Display a question.
    """
    print(question[QUESTION_NAME])
    print(question[QUESTION])
    print("\nOptions:")
    for i in range(question[ANSWERS].__len__()):
        print(f"{i + 1}. {question[ANSWERS][i]}")

def get_user_choice(prompt: str) -> int:
    """
    Prompt the user to select an option until they anter a valid integer between
    1 and the number of answer options inclusive.
    :return: the user's choice.
    """
    while True:
        try:
            choice = int(input(prompt))
            if (choice > 0) and (choice <= NUMBER_OF_ANSWER_OPTIONS):
                return choice - 1
        except ValueError:
            continue

# Load questions.
try:
    questions = load_questions()
except OSError as e:
    abend(e)

# Start quiz
name = input("Hi! welcome to the quiz. Please enter your name to begin: ")

# Ask questions
score = 0
TRIES = 3
for question in questions:
    print_question(question)
    for i in range(TRIES):
        choice = get_user_choice("Please select an option: ")
        if question[ANSWERS].index(question[CORRECT_ANSWER]) == choice:
            score += 1
            print("Correct!")
            break
        else:
            print("Incorrect.")
            if i < (TRIES - 1):
                print(TRIES - i - 1, "tries left.")

print("Your score:", score, "out of", questions.__len__())

# Save score
SCORES_FILE = "quiz_scores.txt"

try:
    score_file = open(SCORES_FILE, "a")
    record = f"Player: {name};Score: {score};Time: {datetime.datetime.now()}"
    score_file.write(record)
    print("Score saved.")
except OSError:
    abend("Failed to save score.")
finally:
    score_file.close()