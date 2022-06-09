n=int(input())
arr=list(map(int,input().split()))
k=int(input())
x=0
for i in range(len(arr)):
    if arr[i]==k:
        print(i)
        x=1
        break
if x==0:
    print("-1")