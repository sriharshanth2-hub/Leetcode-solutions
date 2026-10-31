class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res +=(i+1) *(27-(ord(s[i])-96))
        return res