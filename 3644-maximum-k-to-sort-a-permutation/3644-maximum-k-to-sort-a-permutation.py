class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = None
        
        for i, val in enumerate(nums):
            if val != i:
                if ans is None:
                    ans = val
                else:
                    ans &= val
                    
        return 0 if ans is None else ans