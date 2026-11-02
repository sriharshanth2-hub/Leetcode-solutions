class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        x = nums[::-1]
        ans = [j for j in nums]
        for i in x :
            ans.append(i)
        return ans