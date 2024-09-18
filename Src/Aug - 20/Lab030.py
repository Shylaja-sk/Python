# Grade calculatory - imp interview question
# to calculate and display the letter grade for given numberic scores (eg. A, B, C, D or F)  based on following grade scale
# A: 90 - 100
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: 0-59

# Login buildig formula
# user inputs - score - int
# o\p - string

score = int(input("Enter your score\n"))
if score >= 90 and score <= 100:
    grade = "A"
    print("Your grade is ", grade)
elif score >= 80 and score <= 89:
    grade = "B"
    print("Your grade is ", grade)
elif score >= 70 and score <= 79:
    grade = "C"
    print("Your grade is ", grade)
elif score >= 60 and score <= 69:
    grade = "D"
    print("Your grade is ", grade)
else:
    print("Your grade is F")


    #simplified chain is also possible

