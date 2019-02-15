# Convert lb to kg
# 2/15/2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Darian Lambert
#

#Assign a variable to the input that a user will enter via keyboard.
#Add the formula for the converter.
#Display the result.
#


lb = float(input('Enter an amount (in lbs): '))
kg = lb / 2.2046
print(lb, 'lbs is', format(kg, '.2f'), 'kg')


input('Press ENTER to exit')
