#CTI-110
#M3T1 - Areas of Rectangle
#Oliver Hollis
#11-09-2017
#
#Input the lenght and width of Rectangles
rect_lenght1 = int(input('Enter the lenght of Rectangle 1: '))
rect_width1 = int(input('Enter the lenght of Rectangle 1: '))

rect_lenght2 = int(input('Enter the lenght of Rectangle 2: '))
rect_width2 = int(input('Enter the lenght of Rectangle 2: '))

# Caculate the Areas of the Rectangles
area1 = rect_lenght1 * rect_width1
area2 = rect_lenght2 * rect_width2

# Determine which rectangle has a greater area
if area1 > area2:
    print('Rectangle 1 has a greater area than Reactangle 2')
elif area1 < area2:
    print('Rectangle 2 has a greater area than Reactangle 1')
else:
    print('Both have the same area')
    
