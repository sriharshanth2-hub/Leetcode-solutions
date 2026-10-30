class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r: 
                summed = nums[i] + nums[l] + nums[r]

                if summed > 0:
                    r -= 1
                elif summed < 0:
                    l += 1
                else:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1


                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        
        return out