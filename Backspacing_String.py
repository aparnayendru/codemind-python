s=input()
t=input()
a=[]
b=[]
for i in range(len(s)):
    if s[i]=='#':
        a.pop()
    else:
        a.append(s[i])
for i in range(len(t)):
    if t[i]=='#':
        b.pop()
    else:
        b.append(t[i])
if a==b:
    print("True")
else:
    print("False")
        