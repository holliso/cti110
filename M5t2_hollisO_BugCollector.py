#CTI-110
#M5T2 - Bug Collector
#Oliver Hollis
#09-10-2017

def main():
    
    # bug collector collects bugs every day for 7 days
    # calculate a running total of the number of bugs
    # collected during the 7 day
    # program should ask for the number of bugs collected for that day
    # program should display the total number of bugs collected 


    # how many bugs collected
    bugsCollected = 0

    # Ask user how many bugs collected in 7 days
    for num in range (1,8):
        day_bugs = int(input("How many bugs did you collect today:"))
        bugsCollected = bugsCollected + day_bugs
    
    print("the total number of bugs collected",bugsCollected)
    
main()
