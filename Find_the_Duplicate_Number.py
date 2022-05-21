n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    count=0
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            count+=1
    if count>0:
        print(arr[i],end=' ')