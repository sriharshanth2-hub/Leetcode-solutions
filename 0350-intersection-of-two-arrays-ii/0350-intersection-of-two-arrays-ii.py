class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count = {}
        for n in nums1:
            count[n] = count.get(n, 0) + 1

        result = []
        for n in nums2:
            if count.get(n, 0) > 0:
                result.append(n)
                count[n] -= 1
        return result