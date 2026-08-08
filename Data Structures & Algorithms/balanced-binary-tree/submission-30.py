# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
      
        def search(current):
            if not current:
                return 0 

            leftH = search(current.left)
            rightH = search(current.right)

            if (abs(leftH - rightH) > 1 or leftH == -1 or rightH == -1):
                return -1
            return 1 + max(leftH, rightH)

        return search(root) != -1
        
     
        
       
        