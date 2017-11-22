
# CTI-110
# M6HW1 - TestGrades
# Oliver Hollis
# 12-19-2017



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
	



# Main function area for input of grades and print

def main():
    total = 0
    avg=0
    letter_grades =0
    user_num = []

# Input of 5 grades and caculation thier average  
    
    number1 = float(input("Enter grade 1: "))
    number2 = float(input("Enter grade 2: "))
    number3 = float(input("Enter grade 3: "))
    number4 = float(input("Enter grade 4: "))
    number5 = float(input("Enter grade 5: "))
    for number in (number1, number2,number3, number4, number5 ):
        total += number 
    avg = total/5

# Printing the average and grades entered    
    
    print("Your average is a: ", avg,"from these test scores: ", number1, number2,number3, number4, number5 )

# Print letter grade of average   
    
    print ( avg,  "is", determine_score(letter_grades, avg))    
    
# I got the letter grade for  "number1" entered, everthing else was a tuple    
    
    print ( str(number1) , cal_average(number1,number2,number3, number4, number5))
    
    # THIS DID NO WORK
    #print (str(number2) + cal_average(number1,number2,number3, number4, number5))
    #print (str(number3) + cal_average(number1,number2,number3, number4, number5))
    #print (str(number4) + cal_average(number1,number2,number3, number4, number5))
    #print (str(number5) + cal_average(number1,number2,number3, number4, number5))
    
    cal_average(number1, number2,number3, number4, number5  )
  
# When I used the cal_average function, it would not return 
# (avg) to determine_score function, i used function to assigned
# letter grade to number1,number2,number3, number4, number5

def cal_average(number1, number2,number3, number4, number5   ):
    user_num = 0
    user_num = (int(float(number1)))
   
    if 90 <= user_num  <= 100:
        return ('an A')
    elif 80 <= user_num <= 89:
        return ('a B')
    elif 70 <= user_num <= 79:
        return ('a C')
    elif 60 <= user_num <= 69:
        return ('a D')
    elif 1 <= user_num  <=59:
        return ('a F')   
    if user_num == 0: 
        
        total += user_num   
        
        counter += 5
        
        return number1, number2   
        
# Function to determine the letter grade of avg and grades entered     

def determine_score(letter_grades,avg):

# I used this (int(float(number1))) and it returned the correct
# letter grade for number 1, any other format return a tuple, i.e.
# (int(float(number1,number2, number3, number4, number5,)))
        
    letter_grades = (avg)
        
    if 90 <= letter_grades <= 100:
        return ('an A')
    elif 80 <= letter_grades <= 89:
        return ('a B')
    elif 70 <= letter_grades <= 79:
        return ('a C')
    elif 60 <= letter_grades <= 69:
        return ('a D')
    elif 1 <= letter_grades  <=59:
        return ('a F')   
    if letter_grades == 0: 
        total += test_grades   
        counter += 5
        return avg     

main()
