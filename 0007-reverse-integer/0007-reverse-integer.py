class Solution:
    def reverse(self, x: int) -> int:
        a = []
        if x < 0 :
            x = -x
            z = str(x)
            a.append("-")
            for i in range(len(z)-1,-1,-1) :
                a.append(z[i])
        else :
            z = str(x)
            for i in range(len(z)-1,-1,-1) :
                a.append(z[i])
        result = int("".join(a))
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result