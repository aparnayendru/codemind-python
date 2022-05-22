s=input()
a=0
b=0
for ch in s:
    if ch=='z':
        a=a+1
    elif ch=='o':
        b=b+1
if b==2*a:
    print("Yes")
else:
    print("No")