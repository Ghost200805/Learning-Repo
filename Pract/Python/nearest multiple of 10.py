def roundToNearest(s: str) -> str:
    a = 0
    b = 0
    s = int(s)
    for i in range(0,s+10,10):
        if s == i:
            return s
        if s>=i:
            a = i
        else:
            b = i
            break
    if s-a>b-s:
        return b
    else:
        return a
print(roundToNearest("126"))