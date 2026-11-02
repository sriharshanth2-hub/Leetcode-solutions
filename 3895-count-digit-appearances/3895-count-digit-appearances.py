class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        z = str(digit)
        for i in nums :
            x = str(i)
            count += x.count(z)
        return count