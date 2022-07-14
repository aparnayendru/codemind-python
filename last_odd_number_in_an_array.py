n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)-1,-1,-1):
    if arr[i]%2!=0:
        print(arr[i])
        break