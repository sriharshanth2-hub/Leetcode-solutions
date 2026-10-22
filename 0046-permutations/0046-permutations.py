from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        a = []
        for p in permutations(nums) :
                a.append(list(p))
        return a