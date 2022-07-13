n=int(input())
arr=list(map(int,input().split()))
y=0
x=[]
for i in range(len(arr)):
    count=1
    if arr[i]==-1:
        continue
    else:
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                count+=1
                arr[j]=-1
    if count==arr[i]:
        y=1
        x.append(arr[i])
if y==0:
    print("-1")
else:
    print(min(x),end=" ")
    print(max(x),end=" ")
        