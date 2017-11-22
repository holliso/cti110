# -*- coding: utf-8 -*-
# CTI-110
# M6HW1 - TestGrades
# Oliver Hollis
# 12-11-2017



#  Write the following functions for the program:
#  main() – this function will control the main flow of the 
#  program. It will call the next two functions to do most of 
#  the work. It should  also hold the input() commands to 
#  allow the user to type in grades.

#  calc_average() – this function should accept five test scores 
#  (int or float) as arguments, and return the average of the scores.

#  (In order to calculate an average, you should take the total of 
#  all grades,and then divide it by the number of grades.)

#  determine_grade() – This function should accept a test score 
#  (int or float) as an argument and return a letter grade for 
#  the score. Use the ten-point grading scale you used in a 
#  previous assignment (90-100 for A, 80-89 for B,and so on). 
#  The letter grade, a string, should be A, B, C, D, or F.
	

def main():
    print("Hello, Hope You're Passing")
    num=0
    avg=0
    grd=0
    calc_average(num)
    
    avg = determine_grade(grd)
    
    
def calc_average(num):
    num=0
    num = int(input('Please enter the # of grades being entered: '))
    total_sum = 0
    for n in range(num):
        numbers = int(input('Enter grades : '))
        total_sum += numbers

    avg = total_sum/num
    
    print('Out of ', num, 'grades entered your average is: ', avg)
    return avg   

def determine_grade(grd):
    if grd >= 90 and grd <= 100:
        print ('A')
    elif grd >= 80 and grd <= 89:
        print ('B')
    elif grd >= 70 and grd <= 79:
        print ('C')
    elif grd >= 60 and grd <= 69:
        print ('D')
    else:
        return ('F')

main()
