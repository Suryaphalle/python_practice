'''
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.


love6(6, 4) = True
love6(4, 5) = False
love6(1, 5) = True'''

def love6(a, b):
  sum = a+b
  diff = abs(a-b)
  if a == 6 or b == 6:
    return True
  else:
    if sum == 6 or diff == 6:
      return True
    else:
      return False

def test_love6():
    assert love6(6, 4) == True
    assert love6(4, 5) == False
    assert love6(1, 5) == True
test_love6()    