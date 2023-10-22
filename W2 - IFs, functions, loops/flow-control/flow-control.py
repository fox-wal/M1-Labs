# 1. Even or Odd
def Task_1():
    # Assume that the user inputs a valid integer
    number = int(input("Enter a number: "))
    # Check if divisible by 2
    if (number % 2) == 0:
        print("Even")
    else:    
        print("Odd")

# 2. Multiple of
def Task_2():
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter another number: "))
    
    print(number_1, "is ")
    # Check if number_1 is a multiple of number_2
    if (number_1 % number_2) != 0:
        print("not ")
    print("a multiple of", number_2)

# 3. Absolute
def Task_3():
    number = float(input("Enter a number: "))
    
    print("Absolute value: ")

    if number < 0:
        print(number * -1)
    print(number)

def Task_4():
    grade = int(input("Enter a grade: "))
    if grade == 0:
        print("Zero")
    elif grade == 1:
        print("Low Fail")
    elif grade == 2:
        print("Mid Fail")
    elif grade == 3:
        print("Marginal Fail")
    elif grade == 4:
        print("Low 3rd")
    elif grade == 5:
        print("Mid 3rd")
    elif grade == 6:
        print("High 3rd")
    elif grade == 7:
        print("Low 2:2")
    elif grade == 8:
        print("Mid 2:2")
    elif grade == 9:
        print("High 2:2")
    elif grade == 10:
        print("Low 2:1")
    elif grade == 11:
        print("Mid 2:1")
    elif grade == 12:
        print("High 2:1")
    elif grade == 13:
        print("Low 1st")
    elif grade == 14:
        print("Mid 1st")
    elif grade == 15:
        print("High 1st")
    elif grade == 16:
        print("Exceptional 1st")
    else:
        print("Invalid grade.")

def Task_4_improved():
    grade = int(input("Enter a grade: "))

    grade_scale = ""
    grade_class = ""

    # Determine scale
    if grade == 3:
        grade_scale = "Marginal"
    elif grade == 16:
        grade_scale = "Exceptional"
    elif (grade % 3) == 1:
        grade_scale = "Low"
    elif (grade % 3) == 2:
        grade_scale = "Mid"
    elif (grade % 3) == 0:
        grade_scale = "High"

    # Determine class
    if grade == 0:
        grade_class = "Zero"
    if grade <= 3:
        grade_class = "Fail"
    elif grade <= 6:
        grade_class = "3rd"
    elif grade <= 9:
        grade_class = "2:2"
    elif grade <= 12:
        grade_class = "2:1"
    elif grade <= 16:
        grade_class = "1st"
    
    # Output
    print(grade_scale, grade_class)