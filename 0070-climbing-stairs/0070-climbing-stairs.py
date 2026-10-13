class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 :
            return 1
        if n == 2 :
            return 2
        l = 2
        lb = 1
        ways = 0
        for i in range(3,n+1) :
            ways = l + lb
            lb = l
            l = ways
        return ways