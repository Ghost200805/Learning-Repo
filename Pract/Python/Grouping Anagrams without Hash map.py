def groupAnagrams(strs: list[str]) -> list[list[str]]:
    a = []
    b = {}
    f = {}
    c = []
    n = 0
    m = 0
    for i in range(len(strs)):
        for g in a:
            for k in g:
                if strs[i]==k:
                    n = 1
        if n==1:
            n = 0
            continue  
        c.append(strs[i])
        for j in strs[i]:
            if j not in b:
                b[j]=0
            b[j]+=1
        f = b.copy()
        for k in range(len(strs)):
            if k!=i and len(strs[k])==len(strs[i]):
                for g in a:
                    for j in g:
                        if strs[k] == j:
                            n = 1
                if n == 0:
                    for z in strs[k]:
                        if z in b:
                            if b[z]>0:
                                b[z]-=1
                            else:
                                m = 1
                        else:
                            m = 1
                    if m == 0:
                        c.append(strs[k])
                    m = 0
                n = 0
                b = f.copy()
        a.append(c)
        b = {}
        c = []
    for i in a:
        i.sort()
    a.sort()
    return a

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))