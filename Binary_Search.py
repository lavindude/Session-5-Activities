num = int(input("Pick a number between 1 and 1000 (inclusive) and I will try and guess it: "))
range = 1000
chkpt_1 = 1
chkpt_2 = 1000
keep_guessing = True

between = int(input("Is your number between 1 and 500? "))

if between == 'y':
    chkpt_2 = 500
else:
    chkpt_1 = 500

while keep_guessing:
    between = int(input("Is your number between "))