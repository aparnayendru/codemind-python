n=int(input())
a=1
c=0
while a*a<=n:
    if a*a==n:
        c=1
        print("True")
        break
    a+=1
if c==0:
    print("False")
    