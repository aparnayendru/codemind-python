s=input()
x=[]
sp=[]
spe=[]
for i in range(len(s)):
    if s[i].isalpha():
        x.append(s[i])
    else:
        sp.append(s[i])
        spe.append(i)
rev=x[::-1]
for i in range(len(sp)):
    rev.insert(spe[i],sp[i])
print(*rev,sep='')
