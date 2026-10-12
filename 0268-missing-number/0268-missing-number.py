class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_a = sum(nums)
        total = 0
        for i in range(n+1) :
            total += i
        return total - total_a