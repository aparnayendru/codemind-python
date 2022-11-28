s=input().lower()
s=s.replace(" ","")
a=''
for i in set(s):
    #if s.count(i)==1:
        a+=i
a=list(a)
print(len(a))
