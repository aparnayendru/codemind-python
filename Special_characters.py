s=input()
x="[@_!#$%^&*()<>?/|}{~:]"
even=[]
odd=[]
c=0
for i in s:
    if i in x:
        c+=1
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            even.append(k)
        else:
            odd.append(k)
if c%2==0:
    i=0
    j=0
    while i<len(even) or j<len(odd):
        if i<len(even):
            print(even[i],end="")
            i+=1
        if j<len(odd):
            print(odd[j],end="")
            j+=1
else:
    i=0
    j=0
    while i<len(even) or j<len(odd):
        if j<len(odd):
            print(odd[i],end="")
            j+=1
        if i<len(even):
            print(even[i],end="")
            i+=1
