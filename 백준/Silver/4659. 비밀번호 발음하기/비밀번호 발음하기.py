c = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
v = ['a', 'e', 'i', 'o', 'u']
while True :
    v_count = 0
    c_count = 0
    no = 0
    yes1 = 0
    s = str(input())
    if s == "end" :
      break
    for i in range(len(s)):
        if c.count(s[i]) == 1:
            c_count += 1
            v_count = 0
        if v.count((s[i])) == 1:
            v_count += 1
            c_count = 0
            yes1 = 1
        if i != 0:
            if s[i] == s[i-1]:
                if s[i] != 'e' and s[i] != 'o':
                    no += 1
                else:
                    v_count -= 1
        if v_count == 3 or c_count == 3:
            no += 1
    if yes1 == 1 and no == 0:
        print("<{}> is acceptable.".format(s))
    else:
        print("<{}> is not acceptable.".format(s))