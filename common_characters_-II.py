s=input().lower()
s=s.replace(" ","")
#print(s)
t=input().lower()
t=t.replace(" ","")
a=[]
x=0
#print(t)
if len(s)>len(t):
    for ch in set(s):
        if ch in set(t):
           a.append(ch)
    else:
        print(len(a))
else:
    for ch in set(t):
        if ch in set(s):
            a.append(ch)
            
    else:
        print(len(a))
