s=input()
l=[]
k=[]
ind=[]
for i in range(len(s)):
    if s[i].isalpha():
        l.append(s[i])
    else:
        k.append(s[i])
        ind.append(i)
l.sort()
for i in range(len(k)):
    l.insert(ind[i],k[i])
for i in l:
    print(i,end="")