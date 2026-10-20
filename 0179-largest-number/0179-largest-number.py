from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(a, b):
            if a+b > b+a:
                return -1
            return 1

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(compare))
        result = ''.join(nums)
        return '0' if result[0] == '0' else result