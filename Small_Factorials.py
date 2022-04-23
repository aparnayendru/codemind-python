t=int(input())
prod=1
while t>0:
    prod=1
    n=int(input())
    for i in range(n,0,-1):
        prod=prod*i
    print(prod)
    t=t-1