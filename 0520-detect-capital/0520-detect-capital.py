class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        iscap = False
        if word.isupper() :
            iscap = True
        elif word.islower() :
            iscap = True
        elif word.istitle() :
            iscap = True
        return iscap