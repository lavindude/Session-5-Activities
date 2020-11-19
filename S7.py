''' (NOT DONE)
Problem 1: Synthetic (exponent and coeffient of the x 
you're dividing by must be 1)
'''

highest_degree = int(input("Highest degree of function: "))
numbers = list()

for i in range(highest_degree, -1, -1):
    coef = int(input("Enter " + str(i) + "st coefficient: "))
    numbers.append(coef)

div = int(input("What would you like to divide by? (Example: enter 2 for x-2)"))

def synthetic(numbers, div):
    ret_list = list()