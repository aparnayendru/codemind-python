n=int(input())
arr=list(map(int,input().split()))
k=int(input())
count=0
for i in range(len(arr)):
    if k==arr[i]:
        count=1
        break
if count==0:
    print("False")
else:
    print("True")