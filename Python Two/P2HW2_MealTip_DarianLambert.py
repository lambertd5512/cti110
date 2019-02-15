# When given meal cost, calculates the meal total including gratuity
# 2/15/2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Darian Lambert
#

#Add title
#Assign a variable to the total cost, using input
#Add calculations for tip percentage, and add that to total
#Display the results
#
print('Tip Calculator')
meal =float(input('Enter the meal cost to receive the total cost (including tip):'))
fift= (.15 * meal) + meal
eigt= (.18 * meal) + meal
twet =(.20 * meal) + meal
print ('15%=$', format(fift, '.2f'))
print ('18%=$', format(eigt, '.2f'))
print ('20%=$', format(twet, '.2f'))

input('Press ENTER to exit')
