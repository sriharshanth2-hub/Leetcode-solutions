# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        curr = root
        while curr:
            if val == curr.val:
                return curr
            curr = curr.left if val < curr.val else curr.right
        return None


