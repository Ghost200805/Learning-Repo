def isIsomorphic(s: str, t: str) -> bool:
    a = {}
    b = {}
    if len(s)==len(t):
        d = 0
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]]=0
            if t[i]  not in b:
                b[t[i]] = 0
            b[t[i]]+=1
            a[s[i]]+=1
        if len(a)==len(b):
            return True
        return False
    return False
print(isIsomorphic(s = "egg",t = "add"))