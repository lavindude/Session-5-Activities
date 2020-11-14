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

