class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        x = []
        for w in s :
            x.append(w[::-1])
        return " ".join(x)