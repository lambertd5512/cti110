# Given length and width of two rectangles, displays and compares the area of the two.
# 2/26/2019
# CTI-110 P3T1 - Areas of Rectangles
# Darian Lambert
#

#Restart the program
bloop='y' or 'Y'
while bloop == 'y' or bloop == 'Y':
    
#Input length and width of rectangle 1
    length1 = int(input('Enter the length of rectangle 1: '))
    width1 = int(input('Enter the width of rectangle 1: '))
#Calculate the area of rectangle 1
    area1 = length1 * width1
#Display the area of rectangle 1
    print ('The area of rectangle 1 is: ' + str(area1))
#Input length and width of rectangle 2
    length2 = int(input('Enter the length of rectangle 2: '))
    width2 = int(input('Enter the width of rectangle 2: '))
#Calculate the area of rectangle 2
    area2 = length2 * width2
#Display the area of rectangle 1
    print ('The area of rectangle 2 is: ' + str(area2))
    
#Compare the two - which has the greatest area (Rectangle 1, 2, or neither?)

    if area1 > area2:
        print('Rectangle 1 has the greatest area.')
    elif area2 > area1:
        print('Rectangle 2 has the greatest area.')
    else:
        print('Both have the same area.')
#Ask if user wants to restart program          
    bloop = input('Do you want to restart? (y/n) ')
