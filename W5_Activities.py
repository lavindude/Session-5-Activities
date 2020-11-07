#Problem 1: (Make a calculator)

nums = int(input("How many numbers would you like to use? "))
current_num = float(input("Enter number: "))

for i in range(0, nums - 1):
    operation = input("Enter operation (m, d, a, s): ")
    num = float(input("Enter number: "))

    if operation == "m":
        current_num *= num

    elif operation == "d":
        current_num /= num

    elif operation == "a":
        current_num += num

    else: #assuming this is subtraction
        current_num -= num

print(current_num)


# Problem 2: Using the list [1557, 8, 9, 3, 3, 27, 642, 56, 89, 43, 578, 356, 127], 
#            order it from least to greatest (Don't use og.sort()!!)

# *** note that this is just one of many ways to solve this problem ***

og = [1557, 8, 9, 3, 3, 27, 642, 56, 89, 43, 578, 356, 127]

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