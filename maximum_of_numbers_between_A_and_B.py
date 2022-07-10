n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
x=[]
y=0
for i in range(len(arr)):
    if arr[i]>=a and arr[i]<=b:
        y=1
        x.append(arr[i])
if y==0:
    print("-1")
else:
    print(max(x))