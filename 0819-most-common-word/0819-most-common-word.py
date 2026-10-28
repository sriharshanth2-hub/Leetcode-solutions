class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        x = paragraph.split()
        count = {}
        for i in x :
            count[i] = count.get(i,0)+1
        maxi = 0
        ans = ""
        for i in x :
            if i not in banned and maxi < count[i] :
                maxi = count[i]
                ans = i
        return ans