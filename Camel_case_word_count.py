s=input()
count=1
for i in range(1,len(s)):
    x=ord(s[i])
    if x>=65 and x<=90:
        count+=1
print(count)