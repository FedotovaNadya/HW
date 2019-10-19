dividers=[] 
n=int(input()) 
mystr=""
dividers.append(n) 
for i in range(1,n): 
  if n%i==0: 
    dividers.append(i) 
dividers.sort() 
for i in range(len(dividers)):
  mystr+=str(dividers[i])+" "
print(mystr)
if len(dividers)==2: 
  print("ACHTUNG")
