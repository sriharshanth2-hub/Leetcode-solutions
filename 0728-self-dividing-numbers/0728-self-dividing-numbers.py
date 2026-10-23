class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for i in range(left,right+1) :
            selfie = True
            x = i
            while x > 0 :
                digit = x % 10
                if digit == 0 or i % digit != 0 :
                    selfie = False
                    break
                x //= 10
            if selfie == True :
                ans.append(i)
                
        return ans