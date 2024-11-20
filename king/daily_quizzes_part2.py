# Oct 11, 2024
def boolean_tests(a, b, c, d):
  if not (a and b) or (c < d):
    print("Test passed!")
  result = (a or b) and not (d % c == 0)
  print(result)

def main():
  boolean_tests(True, True, 10, 20)
  boolean_tests(False, True, 12, 20)

# Oct 14, 2024
def new_idea(n):
  for i in range(n):
    for j in range(n):
      print(i, j)

def newer_idea(n):
  for i in range(n):
    for j in range(i):
      print(i, j)

def main():
  new_idea(5)
  newer_idea(5)

# Oct 16, 2024
def main():
  for x in range(5, 40, 6):
    for y in range(2, 45, 8):
      print(x, y)
      print(y > x and y % x == 0)
      
main()

# Oct 18, 2024
n = 5
for i in range(n):
    k = n - i
    for j in range(k*k, 0, -1):
        print('.', end='')
    print()

# Oct 23, 2024
# my_numbers.txt
```
10
20
30
20
10
60
```
data = open('my_numbers.txt')
total = 0
count = 0
for line in data:
  total += int(line)
  count += 1
print(total / count)

# Oct 25, 2024
def write_data(filename, rows):
  file = open(filename, 'w')
  for i in range(rows):
    data = str(random.randint(0, 10)) + ", " + str(random.randint(0, 10))
    file.write(data)

def read_data(filename):
  file = open(filename, 'r')
  for line in file:
    num1, num2 = line.rstrip().split(", ")
    print(num1 + num2)

filename = "test_data.txt"
write_data(filename, 4)
read_data(filename)

# Oct 28, 2024
def write_data(file):
  for i in range(0, 15, 3):
    if i % 2 == 0:
      file.write("o")
    elif i % 3 == 0:
      file.write("x")
    else:
      file.write(".")
  for i in range(22, -1, 7):
    file.write("\n")
  for i in range(3):
    for j in range(5):
      file.write("-")
    file.write("|\n")

file = open("oct28.txt", 'w')
write_data(file)
file.close()
## What is in oct28.txt now?


# Oct 30, 2024
def playing_with_strings(s):
  print("The string is:", s)
  n = len(s)
  new_s = ""
  for i in range(0, len(s), 2):
    print("The letter at index", i, "is", s[i])
    new_s += s[i]
  print("Here is the new string:", new_s)
  for character in new_s:
    print(character)
playing_with_strings("mysterious strings!")

# Nov 4, 2024
def quiz(s):
  print(s[len(s) // 2:3:-1])
  if s.islower() or s.isdigit():
    return 101
  if s.isupper():
    return 202
  if s.isalpha():
    return 303

print(quiz("GoodMorning")) # len(s) = 11
print(quiz("GOODBYE!!")) # len(s) = 9
print(quiz("8675309")) # len(s) = 7
print(quiz("computer")) # len(s) = 8


# Nov 6, 2024
def f(s):
  a = s[::2]
  return a

def g(s):
  a = s[::-1]
  return a
  
def quiz(s):
  new_s = f(s) * 2 + g(s)
  return new_s[2:6] + new_s[-5]

print(quiz("poodles"))

# Nov 8, 2024
a = [1, 3, 5, 9]
b = ['.', '-', ';']
c = [a[1:3] * 2, b[-1] * 4]
d = b[2:3] + a[1:] + c[0:1]
a[0] = 10
b[-3] = '/'
c[0] = 0
print(d[-1])

# Nov 11, 2024
a = [6, 18]
a.append(12)
a.append('12')
b = a
c = b
a[3] = 'hello'
d = b + c + a
d.append("goodbye")
print(d)

# Nov 18, 2024: practice drawing arrows for references, cross out for reassignment
a = [6, 4, 9, 2]
b = a
c = a[:]
a[0] = 12
a[2] = 18
print(b)
print(c)
a = [1, 2, 3, 4]
print(b)
print(c)

# Nov 20, 2024
a = [[6, 8, 7, 5], [2, 7, 1, 3], [6, 9, 4, 4]]
print(len(a))
for i in range(len(a)):
  print(a[i])

for i in range(len(a)):
  for j in range(len(a[i]):
    print(a[i][j], end=" ")
  print()
