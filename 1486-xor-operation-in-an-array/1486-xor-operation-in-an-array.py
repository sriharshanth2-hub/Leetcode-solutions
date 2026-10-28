class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n) :
            nums.append(start + (2*i))
        out = nums[0]
        for i in range(1,n) :
            out = out ^ nums[i]
        return out