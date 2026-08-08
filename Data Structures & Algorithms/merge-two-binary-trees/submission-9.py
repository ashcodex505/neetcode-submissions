# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


        def dfs(node1, node2, currNode): #in the beginning currNode value is 0 left is none right is none 

            if node1 == None and node2 == None:
                return None
            
            elif node1 and node2 == None:
                currNode.val = node1.val
                currNode.left = dfs(node1.left, None, TreeNode())
                currNode.right = dfs(node1.right, None, TreeNode())
            elif node1 == None and node2:
                currNode.val = node2.val
                currNode.left = dfs(None, node2.left, TreeNode())
                currNode.right = dfs(None, node2.right, TreeNode())
            else:
                currNode.val = node1.val + node2.val
                currNode.left = dfs(node1.left, node2.left, TreeNode())
                currNode.right = dfs(node1.right, node2.right, TreeNode())
            
            return currNode

        

        
        currNode = TreeNode()
        return dfs(root1, root2, currNode)
       
            


        

      
        