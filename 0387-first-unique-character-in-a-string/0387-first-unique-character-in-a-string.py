class Solution:
    def firstUniqChar(self, s: str) -> int:
        u = {}
        for i in s :
            u[i] = u.get(i,0)+1
        for i in s :
            if u[i] == 1 :
                return s.index(i)
        else :
            return -1