class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)
        
        for k in range(1, rowIndex):
            # Compute C(rowIndex, k) using C(rowIndex, k - 1)
            row[k] = row[k - 1] * (rowIndex - k + 1) // k
            
        return row