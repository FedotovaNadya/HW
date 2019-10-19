n=int(input())
fib = [0,1]
str=""
if n>=2:
  for i in range(2,n):
    fib.append(fib[i-2]+fib[i-1])
  for i in range (n):
    str+=repr(fib[i])
    if i<n-1:
      str+=", "

elif n==1:
  str=repr(fib[0])
print(str)
