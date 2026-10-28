class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        words = paragraph.split()
        count = {}
        for word in words:
            if word not in banned:
                count[word]=count.get(word,0)+1 

        return max(count,key=count.get)