n=int(input())
arr=list(map(int,input().split()))
k=int(input())
y=0
for i in range(len(arr)):
    count=1
    if arr[i]==-1:
        continue
    else:
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                count+=1
                arr[j]=-1
    if count==k:
        y=1
        print(arr[i],end=" ")
if y==0:
    print("-1")
        