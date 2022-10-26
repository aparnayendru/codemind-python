n=int(input())
for i in range(1,n+1):
    ch=65
    for k in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        s=chr(ch)
        print(s,end="")
        ch=ch+1
    ch=ch-1
    for m in range(1,i):
        ch=ch-1
        s=chr(ch)
        print(s,end="")
    print()