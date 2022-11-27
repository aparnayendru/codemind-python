s=input()
s=s.split()
x='aeiouAEIOU'
for i in range(len(s)):
    s1=''
    if s[i][0] in x:
        s1=s[i]+'ma'
    else:
        s1=s[i][1:]+s[i][0]+'ma'
    for j in range(i+1):
        s1+='a'
    print(s1,end=" ")