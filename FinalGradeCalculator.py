third_quarter_grade = input("Enter the third quarter grade: ")
fourth_quarter_grade = input("Enter the fourth quarter grade: ")

final_grade_third = float(third_quarter_grade) / 3
final_grade_fourth = float(fourth_quarter_grade) / 3 * 2
final_grade = final_grade_third + final_grade_fourth
print(final_grade)
