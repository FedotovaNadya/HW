a=int(input())
dog="@"
if a==1:
  print(dog)
else:
  str=gap*(a-1)+s+gap*(a-1)
  print(str)
  for i in range(2,a+1):
    str=gap*(a-i)+s*(2*i-1)+gap*(a-i)
    print(str)
