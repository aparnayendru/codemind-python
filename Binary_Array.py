n=int(input())
arr=list(map(int,input().split()))
y=0
for i in range(len(arr)):
    if arr[i]!=0 and arr[i]!=1:
        y=1
        break
if y==0:
    print("True")
else:
    print("False")