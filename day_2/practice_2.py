# This is a number magic trick

# Pick a number from 1 - 9
num = input(str("Pick a number from 1-9! "))
print("The user chose: " + num)
num_1 = int(num)

# Multiple by 2
num_2 = num_1 * 2
print(num_2)

# Add 10 to the total
num_3 = num_2 + 10
print(num_3)

# Divide by 2
num_4 = num_3 / 2
print(int(num_4))

# Subtract by the original number
num_5 = int(num_4) - int(num)
print(num_5)

# Final number is 5
if num_5 == 5:
    print("The trick does work!")
else:
    print("I guess this trick doesn't work!")

# Take an user's input
# Assign a new variable for each step
# at the end, use an if statement to see if the final is always 5!