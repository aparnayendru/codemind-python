n=input()
x=n.split()
count=0
for word in x:
    for char in word:
        if char==" ":
            continue
        else:
            count=count+1
print(count)