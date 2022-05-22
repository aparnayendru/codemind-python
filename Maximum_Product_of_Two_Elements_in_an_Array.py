arr=list(map(int,input().split()))
max=0
c=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        c=(arr[i]-1)*(arr[j]-1)
        if c>max:
            max=c
print(max)