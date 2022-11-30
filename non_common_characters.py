s=input().lower()
s=s.replace(" ","")
#print(s)
t=input().lower()
t=t.replace(" ","")
#print(t)
a=[]
x=0
if len(s)>len(t):
    for ch in set(s):
        if ch not in set(t):
           a.append(ch)
           x=1
    for ch in set(t):
        if ch not in set(s):
           a.append(ch)
           x=1
    if x==0:
        print("-1")
    else:
        a.sort()
        for i in a:
            print(i,end="")
else:
    for ch in set(t):
        if ch not in set(s):
            a.append(ch)
            x=1
    for ch in set(s):
        if ch not in set(t):
            a.append(ch)
            x=1
    if x==0:
        print("-1")
    else:
        a.sort()
        for i in a:
            print(i,end="")