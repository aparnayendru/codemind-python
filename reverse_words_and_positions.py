s=input()
x=s.split()
for i in range(len(x)-1,-1,-1):
    t=x[i]
    print(t[::-1],end=" ")
        