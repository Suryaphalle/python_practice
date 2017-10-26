'''
Write a function group(list, size) that take a list and splits into smaller lists of given size.

  output
      >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
      [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
      [[1, 2, 3, 4], [5, 6, 7, 8], [9]]

'''

list = [1,2,3,4,5,6,7,8,9]

def group(list,n):
  l = len(list)
  for i in range(0,l):
    for j in range(i,n):
      print((list[:n])(list[n:(l-n)]))

group(list,3)

'''def group(l, size):
...     return [l[i:i+size] for i in range(0, len(l), size)]
'''