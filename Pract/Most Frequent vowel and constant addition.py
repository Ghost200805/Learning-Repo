class Solution:
    def maxFreqSum(self, s: str) -> int:
        a = ["a","e","i","o","u"]
        b = {}
        s = s.lower()
        c = {}
        for i in s:
            if i in a:
                b[i]=0
            else:
                c[i]=0
        for i in s:
            if i in a:
                b[i]+=1
            else:
                c[i]+=1
        if b:
            d = max(b.values())
        else: 
            d = 0
        if c:
            e = max(c.values())
        else:
            e = 0
        return d+e
print(Solution().maxFreqSum(s = "Shamit"))