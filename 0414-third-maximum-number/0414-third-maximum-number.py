class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        num = list(set(nums))
        if len(num) < 3 :
            return max(num)
        else :
            for i in range(2) :
                maxi = max(num) 
                num.remove(maxi)
            return max(num)