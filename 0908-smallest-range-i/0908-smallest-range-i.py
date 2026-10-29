class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
         z = max(nums)
         y = min(nums)
        
         z -= k
         y += k
         if z-y < 0 :
            return 0
         else :
            return z-y