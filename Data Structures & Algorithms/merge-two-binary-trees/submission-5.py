# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #we are going to create a new node by basically traversing throuhg the two binary trees at the same time and we add the two values 
        resNode = TreeNode()
        def dfs(node1, node2, resNode):
            if node1 == None and node2 == None:
                resNode = None
                return resNode 
            
            if node1 == None and node2:
                resNode.val = node2.val
                resNode.left = dfs(None, node2.left, TreeNode())
                resNode.right = dfs(None, node2.right, TreeNode())
            elif node2 == None and node1:
                resNode.val = node1.val
                resNode.left = dfs(node1.left, None, TreeNode())
                resNode.right = dfs(node1.right, None, TreeNode())
            else:
                
                resNode.val = node2.val + node1.val
                resNode.left = dfs(node1.left,node2.left, TreeNode())
                resNode.right = dfs(node1.right,node2.right, TreeNode())
            
            return resNode
            
            
            


        

        return dfs(root1, root2, resNode)
      
        