s=input()
x="aeiouAEIOU"
count=0
maxi=0
for i in s:
    if i in x:
        count+=1
        maxi=max(count,maxi)
    else:
        count=0
print(maxi)