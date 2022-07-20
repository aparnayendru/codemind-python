s=input()
s=s.lower()
s=s.split()
y="aeiou"
count=0
for words in s:
    if words[0] in y and words[-1] not in y:
        count+=1
print(count)