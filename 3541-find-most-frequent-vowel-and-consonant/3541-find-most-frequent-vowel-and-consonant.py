class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = 0
        c = 0
        vowels = ['a','e','i','o','u']
        for i in set(s) :
            if i in vowels :
                v = max(v,s.count(i))
            else :
                c = max(c,s.count(i))
        return v + c