#  Write the following functions for the program:
#  main() – this function will control the main flow of the program. It will
#  call the next two functions to do most of the work. It should also hold
#  the input() commands to allow the user to type in grades.

#  calc_average() – this function should accept five test scores (int or float)
#  as arguments, and return the average of the scores.

# (In order to calculate an average, you should take the total of all grades,
#  and then divide it by the number of grades.)

#  determine_grade() – This function should accept a test score (int or float)
#  as an argument and return a letter grade for the score. Use the ten-point
#  grading scale you used in a previous assignment (90-100 for A, 80-89 for B,
#  and so on). The letter grade, a string, should be A, B, C, D, or F.

def main():
    


def main():
    cost = float( input("product cost?")
    finalcost= cost = calc_tax(cost)
    print("Cost with tax is:" ,finalcost)

def calc tax(cost

def main():
    name = input("What's your name?")
    ageCategory=int(input("How old are you?"))
    if ageCategory <= 1:
        print ("Hello ", name, " you are an infant.")

    # if a person is older than 1 but younger than 13
    elif ageCategory > 1 and ageCategory < 13:
        print ("Hello ", name, " you are a child.")

    # if a person is at least 13, but less than 20
    elif ageCategory >= 13 and ageCategory < 20:
        print ("Hello ", name, " you are a teenager.")

    # if a person is at least 20, but may be older
    elif ageCategory >= 20:
        print ("Hello ", name, " you are an adult.")
    return name, ageCategory
    

def greet():
    name, ageCategory=main()
    print("Your name is ",name)
    print("You are ",ageCategory,"years old.")
    

greet()
    
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
elif:
   score >= B_SCORE:
      print('Your grade is B.')
      elif
      score >= C_SCORE:
         print('Your grade is C.')
         elif
         score >= D_SCORE:
            print('Your grade is D.')
            elif score >= F_Score:
               print('Your grade is F.')




def main():
    # ask customer to input how many packages they are buying

    packageAmount = int(input("How many packages do you want to buy?"))

    # Caculate the discount
    
    if packageAmount < 10:
        print ('No discount.')
        discount=1.0
    elif packageAmount < 20:
        print ('Your discount is 20%.')
        discount=0.8
    elif packageAmount < 50:
        print ('Your discount is 30%.')
        discount=0.7
    elif packageAmount < 100:
        print ('Your discount is 40%.')
        discount=0.6
    else:
        print ('Your discount is 50%.')
        discount=0.5

    # Show total price with dicount

    total_amount = packageAmount * discount * 99.00

    # Calculate the total price before the discount

    full_price = packageAmount * 99.00
    print ("The amount of your discount is $"),format( full_price - total_amount,".2f")
    print ("Your total purchase price is $"),format( total_amount,".2f")
   

main()

             
