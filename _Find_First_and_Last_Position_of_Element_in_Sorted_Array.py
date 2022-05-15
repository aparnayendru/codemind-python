n=int(input())
arr=list(map(int,input().split()))
k=int(input())
c=0
d=0
for i in range(0,n):
    if arr[i]==k:
        print(i,end=' ')
        c=1
        break
if c==0:
    print("-1",end=' ')
for i in range(n-1,-1,-1):
    if arr[i]==k:
        print(i,end=' ')
        d=1
        break
if d==0:
    print("-1",end=' ')