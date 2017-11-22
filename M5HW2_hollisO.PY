# Oliver Hollis
# CTI 110
# M5HW2: Running Total
# Oct 27 2017

# Write a program that asks the user to enter a series of numbers.
# It should loop, adding these numbers to a running total, until the
# user enters a negative number. When a negative number is entered,
# the program should exit the loop. (It should not add the negative
# number to the total.) The program should then print the total before
# exiting.

def main():

    # the sum equals 0 until added
    
    total = 0

    # user inputs #'s used "float" for decimals input 

    number_entered = float(input( "Enter the first #: "))

    # "while" keeps answering user for info until quit with -1

    while number_entered > -1:
        total = total + number_entered
        number_entered = float(input("Enter next # or a -1 to stop: "))

    # display sum                              

    print("Your total: ", total)
                                  

main()        
