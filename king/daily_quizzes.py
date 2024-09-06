### Trace the code:
# Trace the values of the variables and give the output of the code.

# Sept 4, 2024
first_name = 'Jace'
last_name = 'King'
first_name = last_name
last_name = first_name
print(last_name, first_name)

# Sept 6, 2024
user_input = input("Give me a number between 1 and 100: ") # just make up a number, assume it is an integer
print("You gave:", user_input)
print("Now watch this:")
tens = int(user_input) // 10
ones = int(user_input) % 10
print("There are", tens, "tens and", ones, "ones in", user_input)
