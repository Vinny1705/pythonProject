# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter your score\n"))
if score in range(90, 101):
    print("Grade is A with score: ", score)
elif score in range(80, 90):
    print("Grade is B with score",score)
elif score in range(70,80):
    print("Grade is C with score",score)
elif score in range(60,70):
    print("Grade is D with score",score)
else:
    print("Fail")
