student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
all_heights = 0
for item in student_heights:
    all_heights = all_heights + item

print(all_heights)
avg_heights = all_heights / len(student_heights)

print(round(avg_heights))
