# CTI-110 
# P3HW1 - Color Mixer 
# Darian Lambert
# 2/26/2019
#

#Restart the program
bloop='y' or 'Y'
while bloop == 'y' or bloop == 'Y':
#Input the first color, if it is not a primary color print an error. If a primary color is submitted, move to the second color.
    color1 = (input('Enter the first color. '))
    if color1 == 'red' or color1 == 'blue' or color1 == 'yellow':
#Input the second color, if it is not a primary color, print an error.
        color2 = (input('Enter the second color. '))
    else:
        print ('ERROR: Please enter a primary color.')
        
    if color2 == 'red' or color2 == 'blue' or color2 == 'yellow':
#Display the resulting color
                if color1 =='red' and color2 =='blue':
                    print('When you mix red and blue, you get purple.')
                elif color1 =='red' and color2 == 'yellow':
                    print('When you mix red and yellow, you get orange.')
                elif color1 =='blue' and color2 =='yellow':
                    print('When you mix blue and yellow, you get green.')
                elif color1 =='yellow' and color2 =='red':
                    print('When you mix red and yellow, you get orange.')
                elif color1 =='yellow' and color2 =='blue':
                    print('When you mix blue and yellow, you get green.')
                elif color1 =='blue' and color2 =='red':
                    print('When you mix red and blue, you get purple.')
    else:
        print ('ERROR: Please enter a primary color.')
       

#Ask if user wants to restart program          
    bloop = input('Do you want to restart? (y/n) ')
                


