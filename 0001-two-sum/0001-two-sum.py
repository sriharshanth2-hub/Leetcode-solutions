class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i in range(len(nums)) :
            A_1 = target - nums[i]
            if A_1 in found :
                return found[A_1],i
            found[nums[i]] = i