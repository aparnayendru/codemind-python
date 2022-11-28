s=input().lower()
k=len(s)
m=k//2
x='aeiou'
count=0
for i in range(m):
    if s[i].isalpha() and s[k-i-1].isalpha():
        if (s[i] in x and s[k-i-1] not in x) or (s[i] not in x and s[k-i-1] in x):
            #print(s[i],s[k-i-1],end=" ")
            count+=1
print(count)