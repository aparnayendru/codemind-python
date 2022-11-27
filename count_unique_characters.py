s=input()
s=s.lower()
s=s.replace(" ","")
#print(s)
countt=0
for i in s:
    if s.count(i)==1:
        countt+=1
print(countt)