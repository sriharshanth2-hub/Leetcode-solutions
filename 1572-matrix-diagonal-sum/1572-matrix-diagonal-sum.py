class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        sum1 = 0
        for i in range(n) :
            if i != n-i-1 :
                sum1 += mat[i][i] + mat[i][n-i-1]
            else :
                sum1 += mat[i][i]
        return sum1
        