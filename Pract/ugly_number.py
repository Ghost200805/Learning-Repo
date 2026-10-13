class Solution:
    def isUgly(self, n: int) -> bool:
        l = [2,3,5]
        if n<=0:
            return False
        else:
            for i in l:
                while n%i==0:
                    n//=i
            if n == 1:
                return True
            else:
                return False
print(Solution().isUgly(14))