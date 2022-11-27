n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n,2):
    k=arr[i+1]
    count=1
    while count<=k:
        print(arr[i],end=" ")
        count+=1
