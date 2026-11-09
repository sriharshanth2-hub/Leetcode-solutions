class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)
        a = []
        for i in order :
            if i in friends :
                a.append(i)
        return a