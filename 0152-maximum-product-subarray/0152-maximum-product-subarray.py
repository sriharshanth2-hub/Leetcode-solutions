class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        result = nums[0]
        for i in range(1,len(nums)) :
            temp = cur_max
            cur_max = max(nums[i],nums[i]*cur_max,nums[i]*cur_min)
            cur_min = min(nums[i],nums[i]*temp,cur_min*nums[i])
            result = max(result, cur_max)
        return result

           