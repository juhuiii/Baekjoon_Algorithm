a=input()
p=a.count(":-)")
q=a.count(":-(")
if p==0 and q==0:
    print("none")
elif p==q:
    print("unsure")
elif p>q:
    print("happy")
elif p<q:
    print("sad")