N,m,M,T,R = map(int,input().split())
time = 0
wt = 0
heart = m

if m + T > M :
  print(-1)

else :
  while time < N:
    if heart + T <= M :
      heart += T
      time += 1
      wt += 1
      
    else :
      heart -= R
      if heart < m :
        heart = m
      wt += 1
  print(wt)