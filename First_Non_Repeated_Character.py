for t in range(int(input())):
    n=int(input())
    s=input()
    m=-1
    for i in range(len(s)):
        count=0
        for j in range(len(s)):
            if s[i]==s[j] and i!=j:
                count+=1
        if count==0:
            m=s[i]
            break
    print(m)