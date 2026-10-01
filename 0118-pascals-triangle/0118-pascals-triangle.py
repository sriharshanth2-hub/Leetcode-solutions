class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        row = [1]
        a = []
        for i in range(numRows) :
            a.append(row)
            row = [1] + [row[j]+row[j+1] for j in range(len(row)-1)] + [1]
        return a