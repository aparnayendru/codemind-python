n=int(input())
arr=list(map(int,input().split()))
y=0
for i in range(len(arr)):
    count=0
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            count=1
            arr[j]=-1
    if count==-1:
        arr[i]=-1
for i in range(len(arr)):
    if arr[i]==-1:
        continue
    else:
        y=1
        print(arr[i],end=" ")
if y==0:
    print("-1")
        
        