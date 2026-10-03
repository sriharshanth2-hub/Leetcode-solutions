class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = {}
        left = 0
        freq_window = {}
        n = len(s1)
        m = len(s2)
        for i in s1 :
            freq_s1[i] = freq_s1.get(i,0) + 1
        for right in range(m) :
            freq_window[s2[right]] = freq_window.get(s2[right],0) + 1
            if right-left + 1 > n :
                freq_window[s2[left]] -= 1
                if freq_window[s2[left]] == 0 :
                    del freq_window[s2[left]]
                left += 1
            if freq_window == freq_s1 :
                return True
        else :
            return False
        
        