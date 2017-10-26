import re
def mob_val(num):
  test=re.compile(r'\d{10}',num)
  return "Its num"


result = mob_val(3213213210)
print(result)