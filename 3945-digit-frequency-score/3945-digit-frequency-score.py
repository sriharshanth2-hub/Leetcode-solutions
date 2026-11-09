class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        sn = str(n)
        score = 0
        a = set(sn)

        for i in a:
            c = sn.count(i)
            score += (c * int(i))

        return score
