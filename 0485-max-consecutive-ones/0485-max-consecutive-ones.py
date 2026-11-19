class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        one = 0
        maxi = 0
        for i in range(len(nums)) :
            if nums[i] == 1 :
                one += 1
                maxi = max(maxi,one)
            else :
                one = 0
        return maxi