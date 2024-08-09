# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            current_diameter = left_height + right_height

            self.max_diameter = max(self.max_diameter, current_diameter)

            return 1 + max(left_height, right_height)

        height(root)

        return self.max_diameter