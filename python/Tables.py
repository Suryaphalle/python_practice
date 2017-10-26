def table(num):  
  result = {}

  for i in range(1,11):
    res = num * i 
    yield res

for i in table(int(input("get num :"))):
  print i