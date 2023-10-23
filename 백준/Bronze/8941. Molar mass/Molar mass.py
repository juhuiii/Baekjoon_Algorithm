list = [12.01, 1.008, 16.00, 14.01]
element = ['C', 'H', 'O', 'N']

for i in range(int(input())) :
    a = input()
    x = 0
    y = 0
    count = 0
    for i in range(len(a)) :
      if a[i].isalpha() :
        count = i + 1
        if count == len(a) :
          x += list[element.index(a[i])]
        elif a[count].isalpha() :
          x += list[element.index(a[i])]

        else :
          y = count
          while a[y].isdigit() :
            y += 1
            if y == len(a) :
              break
          if y == len(a) :
            x += list[element.index(a[i])] * int(a[count :])
          else :
            x += list[element.index(a[i])] * int(a[count : y])
    print(f'{x:.3f}')