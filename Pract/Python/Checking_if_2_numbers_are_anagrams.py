def anagram(n1: int, n2: int) -> bool:
    a = {}
    b = {}
    while n1>0:
        if n1%10 in a:
            a[n1%10]+=1
        else:
            a[n1%10]=1
        n1//=10
    while n2>0:
        if n2%10 in b:
            b[n2%10]+=1
        else:
            b[n2%10]=1
        n2//=10
    return a==b

print(anagram(n1=1221,n2=1212))