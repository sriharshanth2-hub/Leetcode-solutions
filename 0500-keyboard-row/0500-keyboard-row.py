class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        f = "qwertyuiop"
        s = "asdfghjkl"
        t = "zxcvbnm"
        v = []
        for i in words :
            x = i.lower()
            if set(x) <= set(f) or set(x) <= set(s) or set(x) <= set(t) :
                v.append(i)
        return v