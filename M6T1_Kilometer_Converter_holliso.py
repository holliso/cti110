#CTI-110
#M6t1 - Kilometer Converter
#Oliver Hollis
#Oct-25-2017

# kilometers from the user
# conversion factor
def main():
    km = int(input("Enter value in kilometers"))
    miles(km)
    
# calculate miles
def miles(kilometers):
    convert = .6214
    miles = (kilometers * convert)
    print(kilometers,"kilometers is equal to this many miles:",miles)      
main()
