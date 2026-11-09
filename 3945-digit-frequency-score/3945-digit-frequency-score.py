class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        count = {}
        total = 0
        z = str(n)
        y = set(z)
        for i in z :
            count[i] = count.get(i,0)+1
        for i in y :
            total += count[i]*int(i)
        return total