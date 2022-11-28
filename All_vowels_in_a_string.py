s=input()
x="aeiou"
y="AEIOU"
a=0
b=0
l=''
u=''
for i in s:
    if i in x and i not in l:
        a+=1
        l+=i
    if i in y and i not in u:
        b+=1
        u+=i
if a==5 or b==5:
    print("True")
else:
    print("False")