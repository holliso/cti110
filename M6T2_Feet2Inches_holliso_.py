#CTI-110
#M6T2 - FeetToInches
#Oliver Hollis
#12-11-2017 

inch_per_foot=12

def main():
    feetToInches(feet)
    print(feet, "number is equal",feetToInches(feet), 'inches') 

# The function that converts feet to inches
def feetToInches(feet):
    return feet * inch_per_foot

# Get the number of feet to be converted to inches.
feet = float(input("Enter the number of feet to convert to inches: "))

# Convert feet to inches
inches = feetToInches(feet)
    
main()
