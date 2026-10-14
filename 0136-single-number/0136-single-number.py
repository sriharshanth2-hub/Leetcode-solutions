class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        s = 0
        for i in nums :
            s = i^s
        return s