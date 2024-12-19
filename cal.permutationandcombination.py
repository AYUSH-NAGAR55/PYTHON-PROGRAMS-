import math 

def calculate_combination(n,r):         
    combination = math.factorial(n)/(math.factorial(r)*math.factorial(n-r)) 
    return combination                  

def calculate_permutation(n,r):   
    permutation = math.factorial(n)/math.factorial(n-r)
    return permutation    

n = int(input("Enter the total number of items (n): "))        
r = int(input("Enter the number of items to choose (r): "))   
combination = calculate_combination(n,r)
permutation = calculate_permutation(n,r)

print(f"Combination (nCr): {combination}")
print(f"Permutation (nPr): {permutation}")


# THE BELOW GIVEN IS THE PROCEDURE AND MEANING OF EACH AND EVERY LINES.

# line 1, imports the math module, which provides functions for mathematical operations, including the factorial function used in this code 

# line 3, defines a function named calculate_combination that takes two arguments n and r.
# line 4, calculate the combination using formula nCr = n!/(r1*(n-r)!), where ! denotes the factorial.
# line 4, the math.factorial function is used to calculate the factorial of a number.
# line 5, return calculated combination value

# line 7, defines a function named calculate_permutation that takes two arguments n and r.
# line 8, calculate the Permutation using formula nPr = n!/(n-r)!, where ! denotes the factorial.
# line 8, the math.factorial function is used to calculate the factorial of a number.
# line 9, return calculated permutation value

# line 11 and 12 prompt the user to enter the value of n and r
# the int function is used to convert the user input to integer

# line 13 and 14, call the calculate_combinations and calculate_permutation functions to calculate the permutation and combination values.

# line 16, print the calculated combination and permutation values to the console.
# the f-string formatting is used to insert the values into the output strings.