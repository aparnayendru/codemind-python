s=input()
x=s.split()
for i in range(len(x)):
    if i%2==0:
        t=x[i]
        print(t[::-1],end=" ")
    else:
        print(x[i],end=" ")