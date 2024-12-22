# WRITE A PYTHON PROGRAM TO PRINT NUMBERS WITHIN A GIVEN RANGE.

import math

lower = int(input(" Please Enter the lower Value: "))
upper = int(input(" Please Enter the upper Value: "))

for Number in range(lower, upper):
    Temp = Number
    Sum = 0
    while(Temp > 0):
        Reminder = Temp % 10
        Factorial = math.factorial(Reminder)
        Sum = Sum + Factorial
        Temp = Temp // 10
    
    if (Sum == Number):
        print(" %d is a Strong Number" %Number)
        

# THE BELOW GIVEN IS THE PROCEDURE AND MEANING OF EACH AND EVERY LINES.

# line 3, imports the math module, which provides functions for mathematical operations, including the factorial function used in this code .
# line 5 and 6, prompt the user to give upper and lower value.
# line 9, store the original number in the temp variable
# line 10, initialise sum to store the sum of factorial of digits
# line 11, loop until all digits are processed
# line 12, extract the last digit
# line 13, calculate the factorial of the digit using math.factorial.
# line 14, add the factorial of the digit to the sum
# line 15, remove the last digit from the temporary number
# line 17, checks if the sum is equal to the original number
# line 18, print the strong number

# OUTPUT
# Please enter the lower limit: 1
# Please enter the upper limit: 1000
# 1 is a Strong Number
# 2 is a Strong Number
# 145 is a Strong Number
