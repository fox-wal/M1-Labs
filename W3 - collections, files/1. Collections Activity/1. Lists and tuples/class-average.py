def calculate_average(grades: list[int]) -> float:
    sum = 0
    for g in grades:
        sum += g
    return sum / len(grades)

def get_grading_scale(grade: float) -> str:
    if ((grade * 10) % 10) > 5:
        grade += 1
    grade //= 1
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
    return grade_scale + " " + grade_class

def calculate_student_averages(student_grades: dict[str, list[int]]) -> dict[str, str]:
    average_grades = {}
    for id, grades in student_grades.items():
        average_grades[id] = get_grading_scale(calculate_average(grades))
    return average_grades

# Test 1
#print(calculate_average([0,3,5,6,6,4,4,5,9,8,7,6,8,7,8]))
#print(calculate_average([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]))

# Test 3
#grade = 9.2 # expected: High 2:2
#grade = 12.6 # expected: Low 1st
#grade = 13.5 # expected: Low 1st
#print(get_grading_scale(grade))

# Test 4
# number_of_students = int(input("number of students: "))
# grades = []
# for i in range(number_of_students):
#     grades.append(float(input(f"Enter grade for student {i + 1}: ")))
# print("Average:", get_grading_scale(calculate_average(grades)))

# Test 5
#print("average grades:", calculate_student_averages({"student 1": [0,3,5,6,6,4,4,5,9,8,7,6,8,7,8], "student 2": [2,3,5,6,6,4,4,5,9,8,7,6,8,7,8], "student 3": [3,3,5,6,6,4,4,5,9,8,7,6,8,7,8], "student 4": [9,9,9,9,9,9,9,5,9,8,7,6,8,7,8]}))
