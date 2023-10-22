def get_grading_scale(grade: float) -> str:
    if grade < 0:
        raise ValueError("grade must not be negative.")

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
