class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        l = []
        for i in range(len(nums)-1,len(nums)-k-1,-1):
            l.append(nums[i])
            nums.pop(i)

        for i in l:
            nums.insert(0,i)
        return nums

a = Solution()
print(a.rotate([3,4,5,6,7,8,9],2))
