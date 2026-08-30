# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #first we did recursvely then we do iteratively 

        # bfs - frist in frist out 
        # dfs - first in last out 
        # we are using dfs but we need to explore all the child nodes of the current node for it to be added to our traversal list so that is the codniton 
       
    #    O(n) #bc of stack r
    #    O(n) cause of array
        # #recursively 
        # res = []

        
        # def dfs(current):
        #     nonlocal res
            
        #     if current and current.left == None and current.right == None:
        #         res.append(current.val)
        #         return 
            
        #     if current == None:
        #         return 
            
        #     dfs(current.left)
        #     dfs(current.right)
        #     res.append(current.val)



        # dfs(root)
     
        # return res


        #iteratively 
        # we need an actuall array as a stack 

        #iterative dfs  - after lunch do this way 
        

        # res = []
        # visited = set()
        # def dfs(current):
        #     nonlocal res 
        #     if current is None:
        #         return

         
        #     dfs(current.left)
        #     dfs(current.right)
        #     res.append(current.val)
            
            
        # dfs(root)
        # return res


        # now we will do iteratively 

        res = []

        # we will need a stack to be able to add and pop 
        stack = []
        stack.append(root)
        visited = set()
        def dfs(root):
            nonlocal stack 
            
            while stack: 
                current = stack.pop()
                if current: 
                    left_done = current.left in visited or current.left == None 
                    right_done = current.right in visited or current.right == None

                if current and left_done and right_done:
                    res.append(current.val)
                    visited.add(current)
                elif current:
                    stack.append(current)
                    stack.append(current.right)
                    stack.append(current.left)
        dfs(root)
        return res                
   




         
       