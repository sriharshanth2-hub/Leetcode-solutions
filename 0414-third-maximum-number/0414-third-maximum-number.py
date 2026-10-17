class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s=set(nums)
        s=sorted(s,reverse=True)
        if len(s)<3:
            return max(s)
        else:
            return s[2]