class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        b = set()
        for i in range(len(nums)-2) :
            target = -1 * nums[i]
            a = set()
            for j in range(i+1,len(nums)) :
                if target - nums[j] in a :
                    b.add((nums[i],target-nums[j],nums[j]))
                a.add(nums[j])
        return [list(t) for t in b]

            
