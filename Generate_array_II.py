n=int(input())
arr=list(map(int,input().split()))
countt=0
for i in range(0,n-1,2):
    k=arr[i]
    m=arr[i+1]
    print((str(k)+" ") * m,end="")