def romanToInt(s: str) -> int:
    a = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    b = 0
    for i in range(len(s)):
        if i+1 < len(s) and a[s[i]]<a[s[i+1]]:
            b-=a[s[i]]
        else:
            b+=a[s[i]]
    return b
print(romanToInt("IVCM"))