'''
Problem 1: Quadratic Formula calculator
'''

import math

times = int(input("How many quadratic equations would you like to calculate? "))

def quadratic(a, b, c):
    #Solution 1:
    numerator = -1 * b + math.sqrt(b ** 2 - 4 * a * c)
    denom = 2 * a
    sol1 = numerator / denom

    #Solution 2:
    numerator = -1 * b - math.sqrt(b ** 2 - 4 * a * c)
    sol2 = numerator / denom

    print("Solutions are x=" + str(sol1) + " and x=" + str(sol2))
    print()

for i in range(0, times):
    a = int(input("Enter the coefficient of x^2: "))
    b = int(input("Enter the coefficient of x: "))
    c = int(input("Enter the constant (c): "))
    print()

    quadratic(a, b, c)

'''
Problem 2 Make a function that gets a list from a user and orders it from least to greatest.
Do not use the .sort() function.
'''

def least_to_greatest(og):
    ordered = False

    while ordered == False:
        #keep swapping numbers until the list is in order
        for i in range(0, len(og) - 1):
            if og[i + 1] < og[i]:
                temp = og[i]
                og[i] = og[i + 1]
                og[i + 1] = temp

        #check if the variable 'ordered' should be changed
        ordered = True
        for k in range(0, len(og) - 1):
            if og[k] > og[k + 1]:
                ordered = False

    print(og)

while True:
    og = list()
    counter = 1
    while True:  
        combined = "Number " + str(counter) + ": "
        item = input(combined)
        if item == '':
            break
        item = float(item)
        og.append(item)
        counter += 1

    least_to_greatest(og)
    print()