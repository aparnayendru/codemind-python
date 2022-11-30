s=input().split()
#print(*s)
for i in range(len(s)):
    #print(s[i])
    for j in range(len(s)):
        if i!=j and len(s[i])<len(s[j]):
            #print(s[i])
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            #print(s[i],s[j])
print(*s)