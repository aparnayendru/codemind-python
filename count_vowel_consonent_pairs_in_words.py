s=input().lower().split()
x='aeiou'
count=0
for i in s:
    k=len(i)
    m=k//2
    for j in range(m):
        if (i[j] in x and i[k-j-1] not in x) or (i[j] not in x and i[k-j-1] in x):
            #print(s[i],s[k-i-1],end=" ")
            count+=1
print(count)
        