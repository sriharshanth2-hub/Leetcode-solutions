class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        left = 0
        if len(nums) == len(set(nums)) :
            return False
        window = set()
        for right in range(len(nums)) :
            if len(window) > k :
                window.remove(nums[left])
                left += 1
            if nums[right] in window :
                return True
            window.add(nums[right])
        return False