class Solution:
    def calPoints(self, operations: list[str]) -> int:
        new = []
        for i in operations:
            if i not in ['+', 'D', 'C']:
                new.append(int(i))
            elif i == '+':
                new.append(new[-1] + new[-2])
            elif i == 'D':
                new.append(new[-1] * 2)
            elif i == 'C':
                new.pop()

        return sum(new)