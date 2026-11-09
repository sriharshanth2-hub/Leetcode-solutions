class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        x = set(friends)
        a = []
        for i in order :
            if i in x :
                a.append(i)
        return a