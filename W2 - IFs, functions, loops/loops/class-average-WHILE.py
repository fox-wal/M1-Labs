NUM_OF_STUDENTS = 15
sum = 0

count = 1
while count <= NUM_OF_STUDENTS:
    sum += int(input(f"{count}. Enter grade: "))
    count += 1

print("Average:", sum / NUM_OF_STUDENTS)