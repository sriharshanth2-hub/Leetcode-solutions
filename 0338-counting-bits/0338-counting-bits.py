class Solution:
    def countBits(self, n: int) -> list[int]:
        no = []
        for i in range(n+1):
            num = i        # copy so you don't destroy i
            count = 0      # reset for each number
            while num > 0:
                count += num & 1
                num >>= 1
            no.append(count)   # append AFTER the while loop finishes
        return no