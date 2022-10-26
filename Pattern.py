n=int(input())
for i in range(1,n+1):
    t=1
    for k in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print(t,end="")
        t=t+1
    t=t-1
    for m in range(1,i):
        t=t-1
        print(t,end="")
    print()