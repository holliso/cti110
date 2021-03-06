#CTI-110
#M6LAB - NAME AND AGE
#Oliver Hollis
#10-30-2017

# Write a program that will ask the user their name and then ask their age. 
# The program should then greet them by name, and tell them their age
#   (infant, child, teenager, or adult).

# You should write the following functions by name:
#   main() which is a void function
#   greet(name) which is a void function
#   ageCategory(age) which returns a string

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
