def sumOfSquares(nums: list[int]) -> int:
    a = 0
    for i in range(1,len(nums)+1):
        if len(nums)%i==0:
            a += nums[i-1]**2
    return a
print(sumOfSquares([1,2,3,4,5,6,7,8]))