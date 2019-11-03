n=int(input("Enter days number: "))
result = []
for i in range(n):
  v=[]
  m=int(input("Enter running number: "))
  for i in range(m):
    TimeS=input()
    TimeS = TimeS.split()
    v.append(int(TimeS[1])/int(TimeS[0]))
  result.append(sum(v))
result.sort()
for i in range(len(result)-1,-1,-1):
  print(result[i])
