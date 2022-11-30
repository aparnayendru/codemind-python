s=input().split()
v='aeiouAEIOU'
for words in s:
    c=[]
    d=[]
    ind=[]
    for i in range(len(words)):
        if words[i].isalpha():
            c.append(words[i])
        else:
            d.append(words[i])
            ind.append(i)
    c.sort()
    for k in range(len(d)):
        c.insert(ind[k],d[k])
    for j in c:
        print(j,end="")
    print(" ",end="")