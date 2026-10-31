class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        while a >= b:
            temp, mult = b, 1
            while a >= (temp << 1):
                temp <<= 1
                mult <<= 1
            a -= temp         # subtract the big chunk
            quotient += mult   # add how many divisors it was worth

        if negative:
            quotient = -quotient

        # 32-bit clamp: -2^31 / -1 = 2^31 overflows
        return min(max(quotient, -2**31), 2**31 - 1)