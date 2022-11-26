s=input()
n=int(input())
a=s.count('a')
le=len(s)
b=n//le
c=n%le
d=b*a
for i in range(c):
    if s[i]=='a':
        d+=1
print(d)
