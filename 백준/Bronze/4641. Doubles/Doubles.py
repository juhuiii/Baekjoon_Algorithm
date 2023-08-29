while True:
    l = list(map(int, input().split()))
    count = 0
    var = 0
  
    if l[0] == -1:
        break
      
    else:
        for i in l[:-1]: 
            var = i * 2
            if var != 0:
                if l.count(var) > 0:
                    count += 1
        print(count) 