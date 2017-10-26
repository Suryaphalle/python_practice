'''A happy number is defined by the following process. Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. 
Display an example of your output here. Find first 8 happy numbers.'''

def sum_of_digits(num):
  add = 0
  while(num > 0):
    r = num % 10
    add += r**2
    num = num/10
  return add  

def happy(n):
    temp = n
    while(temp >= 10):
      temp = sum_of_digits(temp)
    if temp == 1:  
      return "happy number"
    else:
      return "unhappy number"
      
# result = sum_of_digits(232)
# print(result)
happy_number_list = []
for i in range(1,50):
    res=happy(i)
    if res == "happy number":
      happy_number_list.append(i)
print(happy_number_list)

