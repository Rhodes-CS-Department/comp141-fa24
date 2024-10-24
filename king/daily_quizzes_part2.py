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
