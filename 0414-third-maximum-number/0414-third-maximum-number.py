class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        a =set(nums)
        a = sorted(a,reverse = True)
        if len(a)<3:
            return max(a)
        else:
            return a[2]