class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        nums4 = nums2[:n]
        for i in nums4 :
            nums3.append(i)
        nums3.sort()
        nums1[:] = nums3
        