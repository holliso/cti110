#CTI-110
#M3LAB - Areas of Rectangle
#Oliver Hollis
#18-09-2017



# This program takes a number grade and outputs a letter grade.

# system uses 10-point grading scale
A_SCORE = 90  
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60 
F_SCORE = 50

#Get a a 2 digit number from.
score = int(input('Enter your score in numeric value: '))


# Determine the grade.
if score >= A_SCORE:
   print('Your grade is A.')
else:
   score >= B_SCORE:
      print('Your grade is B.')
else:
   score >= C_SCORE:
      print('Your grade is C.')
else: 
   score >= D_SCORE:
      print('Your grade is D.')
else:
   score >= F_Score:
      print('Your grade is F.')
