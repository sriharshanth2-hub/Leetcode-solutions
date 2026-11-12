class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for i in set(jewels) :
            total += stones.count(i)
        return total