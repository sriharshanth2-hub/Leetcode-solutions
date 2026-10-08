class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1 :
            return x
        low = 1
        high = x
        res = 1
        while low <= high :
            mid = low + (high-low) // 2
            if mid*mid <=x :
                res = mid
                low = mid+1
            else :
                high = mid-1
        return res