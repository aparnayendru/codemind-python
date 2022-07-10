n=int(input())
arr=list(map(int,input().split()))
a=[]
b=[]
m=len(arr)//2
for i in range(0,m):
    a.append(arr[i])
for i in range(len(arr)-1,m-1,-1):
    b.append(arr[i])
if len(arr)%2==0:
    for i in range(len(a)):
        print(a[i],end=" ")
        print(b[i],end=" ")
else:
    for i in range(len(a)):
        print(a[i],end=" ")
        print(b[i],end=" ")
    print(b[m],end=" ")
    print("0",end=" ")