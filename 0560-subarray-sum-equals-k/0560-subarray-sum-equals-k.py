class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0 : 1}
        result = 0
        prefixsum = 0
        for i in nums :
            prefixsum += i
            if prefixsum - k in count :
                result += count.get(prefixsum-k)
            count[prefixsum] = count.get(prefixsum, 0) + 1
        return result
        