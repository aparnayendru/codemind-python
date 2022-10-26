n=int(input())
m=0
for i in range(1,n+1):
    for k in range(1,(n-i)+1):
        print('',end=" ")
    for j in range(1,i):
        m-=1
        print(m,end="")
    m=0
    for s in range(1,i+1):
        print(m,end="")
        m+=1
    print()
    m+=1
        
    
