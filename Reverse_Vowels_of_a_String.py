s=input()
x='aeiouAEIOU'
v=[]
a=[]
ai=[]
for i in range(len(s)):
    if s[i] in x:
        v.append(s[i])
    else:
        a.append(s[i])
        ai.append(i)
k=v[::-1]
for i in range(len(a)):
    k.insert(ai[i],a[i])
print(*k,sep="")