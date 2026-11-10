import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = 2
        odd = 1
        i = 0
        while i < n :
            even += 2
            odd += 1
            i += 1
        return math.gcd(odd,even) - 1
        