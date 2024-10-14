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
