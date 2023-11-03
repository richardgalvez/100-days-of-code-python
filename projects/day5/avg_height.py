# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum = 0
student_count = 0

# Add all heights from a list of student_heights
for i in student_heights:
    sum += i

# Get length of array to count students
for n in student_heights:
    student_count += 1

# Divide by the amount of inputs into the array
average_height = round(sum / student_count)

# Outputs
print("total height = " + str(sum))
print("number of students = " + str(student_count))
print("average height = " + str(average_height))