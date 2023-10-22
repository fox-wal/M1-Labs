import statistics as s
import timeit

def calculate_statistics(grades: list[int]) -> dict[str, object]:
    MEAN = "mean"
    MEDIAN = "median"
    MODE = "mode"
    MIN = "min"
    MAX = "max"
    RANGE = "range"
    INTERQUARTILE_RANGE = "interquartile range"
    STANDARD_DEVIATION = "standard deviation"

    grade_stats = {}

    # Averages
    grade_stats[MEAN] = get_grading_scale(s.mean(grades))
    grade_stats[MEDIAN] = get_grading_scale(s.median(grades))
    grade_stats[MODE] = s.mode([get_grading_scale(g) for g in grades])

    # Ranges
    min_grade = min(grades)
    max_grade = max(grades)
    grade_stats[MIN] = get_grading_scale(min_grade)
    grade_stats[MAX] = get_grading_scale(max_grade)
    grade_stats[RANGE] = round(max_grade - min_grade, 2)
    quartiles = s.quantiles(grades)
    grade_stats[INTERQUARTILE_RANGE] = round(quartiles[2] - quartiles[0], 2)
    grade_stats[STANDARD_DEVIATION] = round(s.stdev(grades), 2)
    
    return grade_stats

def get_grading_scale(grade: float) -> str:
    '''
    Converts a numeric `grade` value between 0 and 16 to a grade with a class and scale e.g. "Low 3rd".

    Args:
        grade: Number between 0 and 16 (inclusive).

    Returns:
        The converted `grade`.

    Exceptions:
        ValueError: if `grade` is not within the allowed range
    '''
    MIN = 0
    MAX = 16

    if (grade < MIN) or (grade > MAX):
        raise ValueError(f"Grade must be between {MIN} and {MAX} (inclusive).")

    # Round
    if ((grade * 10) % 10) > 5:
        grade += 1
    grade //= 1

    components = []

    # Determine scale
    if grade == 3:
        components.append("Marginal")
    elif grade == 16:
        components.append("Exceptional")
    elif (grade % 3) == 1:
        components.append("Low")
    elif (grade % 3) == 2:
        components.append("Mid")
    elif (grade % 3) == 0:
        components.append("High")

    # Determine class
    if grade == 0:
        components = ["Zero"]
    elif grade <= 3:
        components.append("Fail")
    elif grade <= 6:
        components.append("3rd")
    elif grade <= 9:
        components.append("2:2")
    elif grade <= 12:
        components.append("2:1")
    elif grade <= 16:
        components.append("1st")
    
    # Output
    return " ".join(components)

#---------------------#
# Program Starts Here #
#---------------------#

setup = '''
from __main__ import calculate_statistics
import random

NUMBER_OF_STUDENTS = 15
MAX_GRADE = 16

grades = []
for i in range(NUMBER_OF_STUDENTS):
    grades.append(random.random() * MAX_GRADE)
'''

NUMBER_OF_TESTS = 100

print(f"min from {NUMBER_OF_TESTS} tests:", min(timeit.repeat(stmt="calculate_statistics(grades)", setup=setup, number=NUMBER_OF_TESTS)))