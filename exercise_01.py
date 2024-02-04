'''
Write a script that takes in a grade from 0-100 inclusive 
(include both 0 and 100 in the range). 
Assuming a normal 10 point grading scale, print off whether the user 
got an A, B, C, D, or F.
'''
# # Take user input inclusive (0-100)
grade = int(input('Enter your grade (0-100): '))

# Check grade range and print appropriate grade/response
if 90 <= grade <= 100:
    print("You got an A! Good stuff!")
elif 80 <= grade < 90:
    print("You got a B. Pretty good!")
elif 70 <= grade < 80:
    print("You got a C. Not bad.")
elif 60 <= grade < 70:
    print("You got a D. Meh.")
else:
    print("You got an F :(")

# ext. sources: https://stackoverflow.com/questions/41950021/typeerror-not-supported-between-instances-of-str-and-int