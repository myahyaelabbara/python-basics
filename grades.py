# grades.py: turns a score from 0 to 100 into a letter grade
score = float(input("Enter a score from 0 to 100: "))
while not 0 <= score <= 100:
    print("That's not possible: scores go from 0 to 100.")
    score = float(input("Try again: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F") 