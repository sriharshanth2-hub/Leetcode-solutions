class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prod = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                total = prod + res[i + j + 1]    # add what's already in this slot
                res[i + j + 1] = total % 10            # the digit that stays here
                res[i + j] += total // 10             # the carry goes to the left slot

        # turn digits into a string and strip leading zeros
        s = ''.join(map(str, res)).lstrip('0')
        return s if s else '0'

