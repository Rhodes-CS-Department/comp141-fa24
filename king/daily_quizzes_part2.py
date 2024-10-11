# Oct 11, 2024
def boolean_tests(a, b, c, d):
  if not (a and b) or (c < d):
    print("Test passed!")
  result = (a or b) and not (d % c == 0)
  print(result)

def main():
  boolean_tests(True, True, 10, 20)
  boolean_tests(False, True, 12, 20)
