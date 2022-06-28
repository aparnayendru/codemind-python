n=int(input())
arr=list(map(int,input().split()))
sum=0
a,b=map(int,input().split())
for i in range(len(arr)):
    if arr[i]>=a and arr[i]<=b:
        print(arr[i],end=' ')
        sum=1
if sum==0:
    print("-1")