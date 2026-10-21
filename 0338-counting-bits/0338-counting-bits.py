class Solution:
    def countBits(self, n: int) -> list[int]:
        sol = [0] * (n+1)
        for i in range(n+1) :
            sol[i] = sol[ i >> 1] + (i&1)
        return sol