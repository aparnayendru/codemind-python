def fib(n):
    n1=0
    n2=1
    n3=n1+n2
    while n3<n:
        n3=n1+n2
        n1=n2
        n2=n3
    if n3==n:
        return True
    else:
        return False
n=int(input())
temp=n
for i in range(n,0,-1):
    if(fib(i)):
        left=i
        break
for i in range(n,10000,1):
    if(fib(i)):
        right=i
        break
c=temp-left
d=right-temp
if c<d:
    print(left)
elif c>d:
    print(right)
else:
    print(left,right,end=" ")
