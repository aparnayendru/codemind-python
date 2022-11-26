s=input()
x='aeiou'
c=0
maxi=0
for i in range(len(s)):
    if s[i] in x:
        c+=1
        maxi=max(c,maxi)
    else:
        c=0
print(maxi)