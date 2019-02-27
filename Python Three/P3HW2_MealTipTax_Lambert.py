# CTI-110 
# P3HW2 - MealTipTax 
# Darian Lambert
# 2/27/19
#

#Restart the program
bloop='y' or 'Y'
while bloop =='y' or bloop=='Y':
#Input the charge for the meal
    meal = float(input('Enter the charge for the meal. '))
#Input the tip percentage user wants to consider, if they enter a % other than 15, 18 or 20, print an error.
    perc = input('Enter the tip percentage you would like to consider. (15%, 18%, or 20%) ')

#When user enters 15%, calculate the tip, tax, and total
    if perc == '15' or perc == '15%':
        tip15 = (.15 * meal)
        tax = (.07 * meal)
        tot15 = meal + tip15 + tax
    
        print ('The tip is $', format(tip15, '.2f'))
        print ('The tax is $', format(tax, '.2f'))
        print ('The total is $', format(tot15, '.2f'))
#When user enters 18%, calculate the tip, tax and total
    elif perc =='18' or perc =='18%':
        tip18 = (.18 * meal)
        tax = (.07 * meal)
        tot18 = meal + tip18 + tax
    
        print ('The tip is $', format(tip18, '.2f'))
        print ('The tax is $', format(tax, '.2f'))
        print ('The total is $', format(tot18, '.2f'))
#When the user enters 20%, calculate the tip, tax and total
    elif perc =='20' or perc =='20%':
        tip20 = (.20 * meal)
        tax = (.07 * meal)
        tot20 = meal + tip20 + tax
    
        print ('The tip is $', format(tip20, '.2f'))
        print ('The tax is $', format(tax, '.2f'))
        print ('The total is $', format(tot20, '.2f'))
#Else, print an error if user enters something other than '15' or '15%', '18' or '18%', '20' or '20%'
    else:
        print ('ERROR: Enter 15%, 18%, or 20% as a tip percentage.')

#Ask user if they want to restart
    bloop=input('Do you want to restart? (y/n)')

