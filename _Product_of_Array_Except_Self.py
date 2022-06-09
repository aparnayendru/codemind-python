n=int(input())
prod=1
arr=list(map(int,input().split()))
for i in range(len(arr)):
    prod=1
    for j in range(len(arr)):
        if i==j:
            continue
        else:
            prod=prod*arr[j]
    print(prod,end=" ")