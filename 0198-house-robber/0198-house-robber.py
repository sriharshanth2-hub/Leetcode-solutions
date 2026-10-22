class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0   # best total up to two houses ago
        prev1 = 0   # best total up to the previous house

        for num in nums:
            cur = max( prev1 , prev2+num )   # skip vs rob
            prev2 = prev1
            prev1 = cur

        return prev1
