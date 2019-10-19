puli=int(input())
chis=[]
znam=[]
#input data
for i in range(puli):
  chis.append(int(input()))
  znam.append(int(input()))
maximum = max(znam)

#common denominator
newZnam=maximum
a=False
while a==False:
  b=True
  for i in znam:
    if newZnam%i!=0:
      b=False
  if b==True:
    a=True
  else:
    newZnam+=maximum
#total chislitel
newChisl=[]
for i in range(len(chis)):
  newChisl.append(int(newZnam/znam[i]*chis[i]))
resChis=sum(newChisl)


#reduction
minimum=min(newZnam,resChis)
a=True
while a:
  for i in range(minimum,1,-1):
    b=False
    if newZnam%i==0 and resChis%i==0:
      newZnam/=i
      resChis/=i
      b=True
    a=b
print(str(int(resChis))+"/"+str(int(newZnam)))
