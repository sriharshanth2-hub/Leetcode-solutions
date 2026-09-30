class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right :
            start = height[left]
            end = height[right]
            curr_height = min(start,end)
            max_area = max(max_area,curr_height*(right-left))
            if start < end :
                left += 1
            else :
                right -= 1
        return max_area

            