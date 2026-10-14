class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        numbers = {}
        for i in nums :
            numbers[i] = numbers.get(i,0)+1
        for key,count in numbers.items() :
            if count ==  1 :
                return key