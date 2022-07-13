n=int(input())
arr=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(len(arr)):
    if arr[i]>k:
        break
    else:
        sum=sum+arr[i]
print(sum)
        