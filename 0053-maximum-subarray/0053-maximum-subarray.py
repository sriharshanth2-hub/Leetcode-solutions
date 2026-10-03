class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       sum = 0
       msum = nums[0]
       for ele in nums :
            sum += ele
            if msum < sum :
                msum = sum
            if sum <= 0 :
                sum = 0
       return msum