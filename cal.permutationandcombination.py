# line 2, imports the math module, which provides functions for mathematical operations, including the factorial function used in this code 
import math 

# line 8, defines a function named calculate_combination that takes two arguments n and r.
# line 9, calculate the combination using formula nCr = n!/(r1*(n-r)!), where ! denotes the factorial.
# line 9, the math.factorial function is used to calculate the factorial of a number.
# line 10, return calculated combination value
def calculate_combination(n,r):         
    combination = math.factorial(n)/(math.factorial(r)*math.factorial(n-r)) 
    return combination                  

# line 16, defines a function named calculate_permutation that takes two arguments n and r.
# line 17, calculate the Permutation using formula nPr = n!/(n-r)!, where ! denotes the factorial.
# line 17, the math.factorial function is used to calculate the factorial of a number.
# line 18, return calculated permutation value
def calculate_permutation(n,r):   
    permutation = math.factorial(n)/math.factorial(n-r)
    return permutation    

n = int(input("Enter the total number of items (n): "))       # line 20 and 21 prompt the user to enter the value of n and r 
r = int(input("Enter the number of items to choose (r): "))   # the int function is used to convert the user input to integer

# the below two lines call the calculate_combinations and calculate_permutation functions to calculate the permutation and combination values.
combination = calculate_combination(n,r)
permutation = calculate_permutation(n,r)

# the below two lines print the calculated combination and permutation values to the console.
# the f-string formatting is used to insert the values into the output strings.
print(f"Combination (nCr): {combination}")
print(f"Permutation (nPr): {permutation}")