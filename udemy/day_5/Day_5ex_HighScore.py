student_scores = input("Input a list of student scores ").split()
student_scores_int = []
for n in student_scores:
    student_scores_int.append(int(n))
highest_score = 0
for i in range(0, len(student_scores_int)):
    if student_scores_int[i] > highest_score:
        highest_score = student_scores_int[i]

print("The highest score is", highest_score)


