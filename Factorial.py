# WRITE A PROGRAM TO PRINT THE FACTORIAL OF A NUMBER USING RECURSION.

def factorial(n):              # funtion to calculate factorial using recursion
    if n == 0 or n == 1 :      # base case: factorial of 0 or 1 is 1
     return 1
    else:
        return n * factorial(n-1)   # recursive case: n! = n*(n-1)!
    
num = int(input("Enter a number: "))
print("Factorial of",num, "is", factorial(num))


# OUTPUT
# Enter a number: 5
# Factorial of 5 is 120