#CTI-110
#M3HW1 - Age Classifier
#Oliver Hollis
#11-09-2017

def main():
    
    #ask user to input age
    age = int(input('Please enter a persons age.'))

    # if a person is 1 or younger
    if age <= 1:
        print ('The person is an infant.')

    # if a person is older than 1 but younger than 13
    elif age > 1 and age < 13:
        print ('The person is a child.')

    # if a person is at least 13, but less than 20
    elif age >= 13 and age < 20:
        print ('The person is a teenager.')

    # if a person is at least 20, but may be older
    elif age >= 20:
        print ('The person is an adult.')

main()
