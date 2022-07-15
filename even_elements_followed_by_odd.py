n=int(input())
arr=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(arr)):
    if arr[i]%2==0:
        a.append(arr[i])
    else:
        b.append(arr[i])
print(*a,end=" ")
print(*b,end=" ")