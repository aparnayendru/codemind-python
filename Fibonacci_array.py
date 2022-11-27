n=int(input())
arr=list(map(int,input().split()))
x=0
y=0
for i in range(2,n):
    if arr[i-2]+arr[i-1]==arr[i]:
        x+=1
    else:
        y=1
        break
if y==0 and x>0:
    print("yes")
else:
    print("no")
