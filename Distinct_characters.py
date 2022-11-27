s=input().lower()
s=s.replace(" ","")
a=''
for i in s:
    if s.count(i)==1:
        a+=i
a=list(a)
a.sort()
for i in a:
    print(i,end="")