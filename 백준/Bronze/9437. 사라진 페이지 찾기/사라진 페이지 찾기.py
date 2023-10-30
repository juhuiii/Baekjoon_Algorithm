while True :
  a = list(map(int, input().split()))
  if a == [0] :
    break
  for i in range(a[0] //4) :
    page = [2 * i + 1, 2 * i + 2, a[0] - 2 * i -1, a[0] - 2 * i]
    if a[1] in page :
      page.remove(a[1])
      print(*page)