# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #DFS approach - stack 
        #your attempt
        # curr = root

        # stack = []
        # stack.append(curr)
        # while len(stack) != 0:
        #     curr = stack.pop()
        #     if curr.left != None or curr.right != None:
        #         if curr.left and curr.left.val >= curr.val:
        #             return False
        #         if curr.right and curr.right.val <= curr.val:
        #             return False
        #     if curr.right:
        #         stack.append(curr.right)
        #     if curr.left:
        #         stack.append(curr.left)
        # return True
        
        #neetcodes attempt
        #recursively 
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return  valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("+inf"));

            



        