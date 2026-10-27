from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        center= 0
        res=0
        for key in counter.keys():
            if counter[key]%2==1:
                center=1
            res+=counter[key]-counter[key]%2
        return res+center