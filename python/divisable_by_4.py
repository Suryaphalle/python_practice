divby4 = []
nondivby4 = []
for x in range(1,100):
  if x % 4 == 0:
    divby4.append(x)
  else:
    nondivby4.append(x)  

print("NO divisiable by 4: " + str(divby4))
print("NO not divisiable by 4 :" + str(nondivby4))