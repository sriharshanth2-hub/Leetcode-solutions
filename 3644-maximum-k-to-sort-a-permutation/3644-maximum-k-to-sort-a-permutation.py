class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        sol = None
        
        for i, val in enumerate(nums):
            if val != i:
                if sol is None:
                    sol = val
                else:
                    sol &= val
                    
        return 0 if sol is None else sol