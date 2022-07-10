n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
max=0
x=0
for i in range(len(arr)):
    if arr[i]>=a and arr[i]<=b:
        continue
    elif arr[i]>max:
        x=1
        max=arr[i]
if x==0:
    print("-1")
else:
    print(max)