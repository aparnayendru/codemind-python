n=int(input())
arr=list(map(int,input().split()))
k=int(input())
max=0
for i in range(len(arr)):
    if arr[i]+k>=max:
        max=arr[i]
        print("True",end=' ')
    else:
        print("False",end=' ')