n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if (arr[j]<arr[i]):
            count=count+1
    print(count,end=' ')