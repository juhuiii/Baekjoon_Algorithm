people=[]
m1,n1=map(int,input().split())
m2,n2=map(int,input().split())
m3,n3=map(int,input().split())
m4,n4=map(int,input().split())
people.append(n1)
people.append(n1-m2+n2)
people.append(n1-m2+n2-m3+n3)
people.append(n1-m2+n2-m3+n3-m4+m4)
people.sort()
print(people[len(people)-1])