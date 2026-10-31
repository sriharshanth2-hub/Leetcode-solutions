class Solution:
    def reverseDegree(self, s: str) -> int:
        num = 0
        for ch in range(len(s)) :
            x = -(ord(s[ch]) - ord('a') - 26)
            num += x*(ch+1)
        return num