NUM_OF_STUDENTS = 15
sum = 0

for s in range(NUM_OF_STUDENTS):
    sum += int(input(f"{s}. Enter grade: "))

print("Average:", sum / NUM_OF_STUDENTS)