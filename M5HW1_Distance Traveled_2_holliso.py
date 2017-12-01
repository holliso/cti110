# Oliver Hollis
# CTI 110
# M5HW1: Distance Traveled
# Oct 27 2017

# The speed of a vehicle, and the number of hours it has traveled.
# The program should then display the distance that the vehicle has
# traveled for each hour of that time period. Your output should be
# displayed in table format.



def main():

    # user input information

    speed_of_vehicle = float( input("What is the speed of the vehicle in mph:"))
    traveling_time = int( input("How many hours has it traveled?:"))
    
    # skipped a line
    
    print()
    
    # label tabs for infomation
                               
    print( "HOURS", "\tDISTANCE TRAVELED")

    # 1-3 hours listed

    for the_hour in range(1, traveling_time +1):

        # formula: distance = speed * time

        distance_traveled = speed_of_vehicle * the_hour
        print( the_hour,'\t',distance_traveled)

main()                 
