def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_digits = 0
    for digit in num_str:
        sum_of_digits += int(digit)**num_digits
    if sum_of_digits == num:
        return True
    else:
        return False

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

print("Armstrong numbers between", lower_limit, "and", upper_limit, "are: ")
for num in range(lower_limit, upper_limit + 1):
  if is_armstrong(num):
    print(num)
    
    
# THE BELOW GIVEN IS THE PROCEDURE AND MEANING OF EACH AND EVERY LINES.

# line 1, function to check if a number is Armstrong
# line 2, convert the number to string to calculate the number of digits
# line 3, calculate the number of digits
# line 4, initialize a variable to store the sum of the digits raised to the power of the number of digits
# line 5, iterate over each digit in the number
# line 6, add the digit raised to the power of the number of digits to the sum
# line 7,8,9,10, checks if the sum is equal to the original number

# line 12 and 13, ask the user for a range of numbers

# line 15,16,17,18, print the armstrong number in the given range


# OUTPUT OF THE ABOVE CODE WILL BE
# Enter the lower limit: 1
# Enter the upper limit: 1000
# Armstrong numbers between 1 and 1000 are:
# 1 2 3 4 5 6 7 8 9 153 370 371 407
