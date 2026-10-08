class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered = ""

        for ch in s:
            if ch.isalnum():
                filtered += ch

        if filtered == filtered[::-1]:
            return True
        else:
            return False