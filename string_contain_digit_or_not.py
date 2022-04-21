s=input()
count=0
for character in s:
    if character.isdigit():
        count+=1
if count==0:
    print("Doesn't contain digit")
else:
    print("Contains"+" "+str(count)+" "+"digit")