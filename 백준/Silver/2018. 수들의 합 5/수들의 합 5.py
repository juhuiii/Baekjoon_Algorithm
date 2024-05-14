import sys
input = sys.stdin.readline

n = int(input())

count = 0
sum = 0
start = 0
end = 0

while end <= n :
  if sum < n :
    end += 1
    sum += end
  elif sum > n :
    sum -= start
    start += 1
  else :
    count += 1
    end += 1
    sum += end

print(count)