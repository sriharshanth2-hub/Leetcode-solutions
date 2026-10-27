class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for i in s :
            count[i] = count.get(i,0) + 1
        longest = 0
        has_odd = False
        for c in count.values():
            longest += (c // 2) * 2   # use all the pairs
            if c % 2 == 1:
                has_odd = True        # one leftover can go in the middle

        return longest + 1 if has_odd else longest