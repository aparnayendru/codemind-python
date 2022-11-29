n=int(input())
arr=list(map(str,input().split()))
l=[]
s=[]
for i in arr:
    l.append(len(i))
a=max(l)
for i in range(n):
    if l[i]==a:
        s.append(arr[i])
print(*s)