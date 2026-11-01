class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base(n: int, b: int) -> str:
            digits = []
            while n > 0:
                digits.append(str(n % b))
                n //= b
            return "".join(reversed(digits))
        for base in range(2, n - 1):  # base from 2 to n - 2 inclusive
            s = to_base(n, base)
            if s != s[::-1]:
                return False

        return True