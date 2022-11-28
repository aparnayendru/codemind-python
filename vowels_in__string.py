s=input()
x="aeiouAEIOU"
y=''
a=0
for i in s:
    if i in x and i not in y:
        a=1
        y+=i
if a==0:
    print("-1")
else:
    for i in y:
        print(i,end=" ")