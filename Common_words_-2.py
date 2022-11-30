s=input().lower().split()
t=input().lower().split()
countt=0
for i in s:
    if s.count(i)==1 and t.count(i)==1:
        countt+=1
print(countt)