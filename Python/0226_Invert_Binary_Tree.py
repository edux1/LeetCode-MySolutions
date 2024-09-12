# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        if root is None:
            return root
        
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root
        