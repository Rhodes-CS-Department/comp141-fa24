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

# Sept 13, 2024
a = 4
b = 6
c = 10
if (a - b) > 0:
  c = c * 2
elif c > 8:
  c = c * 3
if c > (a * b):
  a = a + b
  b = a + b
else:
  c = c / 2
a = a + 1
b = b + 1
c = a + b + c
print(a, b, c)

# Sept 16, 2024
def does_this_change_anything(x, y, z):
  x = y * z
  y = x + y
  z = x * y
  print(x, y, z)

def main():
  a = 10
  b = 9
  c = 12
  does_this_change_anything(a, b, c)
  print(a, b, c)

main()

# Sept 18, 2024
from cs1.graphics import *

def draw_thing(x, y):
    set_color('blue')
    draw_filled_polygon(x + 50, y, 
                        x + 30, y + 80, 
                        x, y + 100, 
                        x + 100, y + 100,
                        x + 70, y + 80)
    set_color('green')
    draw_filled_circle(x + 50, y + 80, 10)
    
def main():
    open_canvas(200, 200)
    draw_thing(0, 0)
    draw_thing(100, 0)
    draw_thing(0, 100)
    draw_thing(100, 100)
    
main()

# Sept 20, 2024
def x(s, t):
  s = 2*t
  t = -s
  value = 10*s + 5*t
  print(value)

def y(s, t):
  s = -s
  t = s / 4
  value = 6*s - 10*t
  print(value)

def m():
  s = 4
  t = 2
  x(s, t)
  x(s, t)
  y(s, t)
  y(2*s, 3*t)

m()

# Sept 23, 2024
def do_i_change_anything(a, b, c):
  x = a + b
  y = b - c
  z = a * b * c
  return x + y + z

def main():
  x = 3
  y = 1
  z = 10
  z = do_i_change_anything(x, y, z)

main()

# Sept 25, 2024
## HINT: there are two erors:
### one "logical" error, preventing the program from doing "what I want" but otherwise invisible
### and one "semantic" error, causing the program to "throw an exception" (if the program ran!)
## can you find both?
def tiny_helper_function_1(x, y):
  return 2 * x - y

def tiny_helper_function_2(x, y):
  return x * y + 1
  
def medium_helper_function(x, y):
  return tiny_helper_function_1(x, y) / tiny_helper_function_2(x, y)

def main():
  a = medium_helper_function(0, 0)
  c = medium_helper_function(1, 1)
  b = medium_helper_function(-1, 1)

# Sept 27, 2024
def countdown(n):
  while n > 0:
    print(n, " ticks left!")
    n -= 1

def main():
  countdown(4)
  countdown(0)

main()

# Sept 30, 2024
## powers of 2:
## 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8182, 16384, 32768, ...
def find_biggest_power_of_2(below):
  guess = 1
  while guess < below:
    guess *= 2
  return guess

def main():
  keep_going = True
  limit = 10000
  while keep_going:
    power = find_biggest_power_of_2(limit)
    print(power)
    limit /= 10
    keep_going = limit > 1
    
main()

# Oct 2, 2024
def helper(n):
  if n % 2 == 0: # n is even
    return n / 2
  else: # n is odd
    return 3*n + 1

def collatz(n):
  n = helper(n) # so we can see what happens when n = 1
  steps = 1
  while n > 1:
    n = helper(n)
    steps += 1
  return steps

def main():
  collatz(1)
  collatz(16)
  collatz(12)

main()
    
# Oct 4, 2024
def my_first_for_loops(a):
  # range syntax: range(start=0, stop, step=1) <- start, step have default values
  ## NOTE: stop is EXCLUDED from the range
  for x in range(a):
    print(x)

  for y in range(2, a, 2):
    print(y)

  for var_name in range(a, 0, -2):
    print(var_name)

def main():
  my_first_for_loop(10)

main()

# Oct 7, 2024
def helper1(x):
  if x < 12:
    return 0
  return 100

def helper2(y):
  result = 0
  for x in range(0, y, 2):
    result += x
  return result

def main():
  a = 5
  b = 3
  iterations = 0
  mystery = True
  while mystery:
    a += 3
    b += 5
    iterations += 1
    mystery = helper1(a) > helper2(b)
  print(iterations)
