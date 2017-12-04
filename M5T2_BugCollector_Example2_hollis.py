#CTI-110
#M5T2 - Bug Collector
#Oliver Hollis
#09-10-2017

def main():
    
    # A bug collector collects bugs every day for 7 days.
    # Calculate a running total of the number of bugscollected during the 7 day.
     
    # The program should ask for the number of bugs collected for that day.
    # program should display the total number of bugs collected. 

    # Days of the week
    daysOfweek = ["Monday", "Tuesday", "Wednseday", "Thursday", "Friday", "Saturday", "Sunday"]

    # How many bugs collected
    bugsCollected = 0

    # Ask user how many bugs collected in 7 days
    for num in range (7):
        print("Today is ",daysOfweek[num])
        day_bugs = int(input("How many bugs did you collect today: "))
        bugsCollected = bugsCollected + day_bugs
    
    print("the total number of bugs collected",bugsCollected)

        
main()
