# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #this type of traveral is basically a depth first search so we should be able to do this 
        res = []

        #append the values of each of the nodes to the res integer array 
        def dfs(curr):
            if curr == None:
                return 
            
            dfs(curr.left)
            dfs(curr.right)
            res.append(curr.val)

        



        dfs(root)

        return res
        