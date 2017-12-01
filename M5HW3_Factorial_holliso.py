# Oliver Hollis
# CTI 110
# M5HW3: FACTORIAL
# Oct 29 2017


# Write a program that asks the user for a nonnegative integer and then uses a 
# loop to calculate the factorial of that number. Display the factorial. 

def main():
	
	# defining varible and user enters number
	
	number_= int( input( "Enter a number: "))

	# conditional loop
	
	while number_ < 1:
		number_ =int (input( "Enter a number: "))
	
	# define factorial

	factorial =1

        # lterative loop sequence that adds the next number
        # and multiply it buy the next number

	for new_number in range( 1, number_ + 1):
		factorial *= new_number

	print("The factorial of ",number_, "is ",factorial)  	

main()
