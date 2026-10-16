class Solution:
    def addDigits(self, num: int) -> int:
        si = [0,1,2,3,4,5,6,7,8,9]
        seen = set()
        while num not in si and num not in seen :
            seen.add(num) 
            total = 0
            while num > 0 :
                digits = num % 10
                total += digits
                num //= 10
            num = total
        if num in si :
            return num
        else :
            return False