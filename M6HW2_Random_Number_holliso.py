# CTI-110
# M6HW1 - Random Number Guess
# Oliver Hollis
# 12-19-2017


# import random library
import random
count = 0

def main():
# function to repeat input 
    play_again()
    
def play_again():    
# in the random range of 1-100 
    number = random.randint(1, 101)
#input of number    
    
    print('Whats the number')
    count = input()
    count = int(count)
    count==count+1
    
# entered number pass through if statements, "While" loop
    
    if count < number:
        print('Number is too low.') 
    if count > number:
        print('number is too high.')
    if count == number:
        print('you are correct')
      
             
main()
