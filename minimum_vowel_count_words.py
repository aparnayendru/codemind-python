s=input().lower().split()
x='aeiou'
count=0
maxx=999
maxi=0
for words in s:
    count=0
    for i in words:
        if i in x:
            count+=1
    if count<maxx:
        maxx=count
for words in s:
    count=0
    for i in words:
        if i in x:
            count+=1
    if count==maxx:
        maxi+=1
print(maxi)