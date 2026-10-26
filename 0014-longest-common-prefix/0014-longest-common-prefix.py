class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""

        for i in range(100):
            for s in strs:
                if i >= len(s):
                    return result

                if s[i] != strs[0][i]:
                    return result

            result += strs[0][i]

        return result

                 

        
        