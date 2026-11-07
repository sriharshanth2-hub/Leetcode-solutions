class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = n
        if n == 1 :
            return 1
        for i in range(1,n+1) :
            if x >= i :
                x -= i
            else :
                return i-1