class Solution:
    def reverseWords(self, s: str) -> str:
        if not s :
            return None
        s = s.split()
        a = []
        for w in s :
            a.append(w[::-1])
        return " ".join(a)