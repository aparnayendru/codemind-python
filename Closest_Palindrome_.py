n=int(input())
temp=n
left=0
right=0
for i in range(n-1,0,-1):
    k=i
    sum=0
    while k>0:
        r=k%10
        sum=sum*10+r
        k=k//10
    if sum==i:
        left=i
        break
for i in range(n+1,10000,1):
    k=i
    sum=0
    while k>0:
        r=k%10
        sum=sum*10+r
        k=k//10
    if sum==i:
        right=i
        break
c=temp-left
d=right-temp
if c<d:
    print(left)
elif d<c:
    print(right)
else:
    print(left,right,end=" ")
