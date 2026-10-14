class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = {}
        z = 0
        for i in nums :
            n[i] = n.get(i,0) + 1
        for key,count in n.items() :
            z = max(count,z) 
        for k, v in n.items() :
            if v == z :
                return k