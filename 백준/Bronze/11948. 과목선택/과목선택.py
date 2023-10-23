a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
l = [ a, b, c, d]
l.remove(min(l))
h = [e,f]
h.remove(min(h))
print(sum(l)+sum(h))