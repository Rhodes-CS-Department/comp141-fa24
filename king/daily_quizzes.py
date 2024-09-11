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

# Sept 9, 2024
a = 10
b = 12
c = 13
if a < b:
  print("red")
else:
  print("blue")
if (a + b) % 2 == 0:
  print(a + b, " is even")
if c % 2 == 0:
  print(c, " is even")
else:
  print("Something is odd...")

# Sept 11, 2024
cond1 = 3 < 4
cond2 = False
if cond1:
  cond2 = True
  print("3 IS less than 4")
elif cond2:
  print("cond2 is True")
else:
  print("Nothing interesting happened.")

if cond1:
  print("3 is STILL less than 4")
if cond2:
  print("cond2 is True")
else:
  print("Still nothing interesting happened.")
