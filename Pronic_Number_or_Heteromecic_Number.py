n=int(input())
count=0
for i in range(1,n+1):
    if i*(i+1)==n:
        count=count+1
if count>0:
    print("YES")
else:
    print("NO")