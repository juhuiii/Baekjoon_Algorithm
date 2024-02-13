a=[]
b=[]
c=[]
for i in range(10):
  t=input()
  for j in range(10):
    if t[j]=='B':a=[i,j]
    if t[j]=='L':b=[i,j]
    if t[j]=='R':c=[i,j]
r=abs(a[0]-b[0])+abs(a[1]-b[1])-1
if a[0]==b[0]==c[0]:
  if a[1]<c[1]<b[1]or a[1]>c[1]>b[1]:r+=2
elif a[1]==b[1]==c[1]:
  if a[0]<c[0]<b[0]or a[0]>c[0]>b[0]:r+=2
print(r)