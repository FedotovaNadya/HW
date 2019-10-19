file = input("Enter file name: ")
file= "input_1.txt"
f = open(file, 'r')
data = {}
fd = f.readlines()
print (fd)
words=[]
for i in range(len(fd)):
  words=fd[i].split()
  for j in range(len(words)):
    words[j]=words[j].lower()
    if words[j] in data:
      data[words[j]] +=1
    else:
      data[words[j]]=1
print(data)

fd=[]
while len(fd)<5:
  max=1
  for i in data:
    if data[i]>max and i not in fd:
      max=data[i]
      word = i
  if word not in fd:
    fd.append(word)
for i in range(len(fd)):
  print(fd[i])
