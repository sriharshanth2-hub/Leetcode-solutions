class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n) :
            x = str(n)[::-1]
            return int(x)
        return abs(reverse(n) - n)