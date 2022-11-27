def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
temp=n
left=0
right=0
c=0
d=0
for i in range(n,1,-1):
    if(prime(i)):
        left=i
        break
for i in range(n+1,10000):
    if prime(i):
        right=i
        break
c=temp-left
d=right-temp
if c<d:
    print(c)
else:
    print(d)
