import tkinter as tk
from tkinter import simpledialog

exam_one = int(simpledialog.askstring("Input"," exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring("Input","exam grade two: ", parent=tk.Tk().withdraw()))

exam_three = int(simpledialog.askstring("Input","exam grade exam_three: ", parent=tk.Tk().withdraw()))

grades = [exam_one,exam_two,exam_three]
sum = 0

for grade in grades:
    sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade is "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
