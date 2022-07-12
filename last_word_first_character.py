s=input()
s=s.split()
y=0
for i in range(len(s)-1,-1,-1):
    x=s[i]
    for ch in x:
        y=1
        print(ch)
        break
    if y==1:
        break