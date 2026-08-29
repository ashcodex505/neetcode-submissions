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

        #iterative dfs 


         
        res = []
        if not root:
            return res

        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()

            if not node:
                continue

            # A node is ready if both children are already done.
            # Missing children count as done.
            left_done = node.left is None or node.left in visited
            right_done = node.right is None or node.right in visited

            if left_done and right_done:
                res.append(node.val)
                visited.add(node)
            else:
                stack.append(node)

                # Push right first, then left.
                # Do NOT push children that are already visited.
                if node.right and node.right not in visited:
                    stack.append(node.right)
                if node.left and node.left not in visited:
                    stack.append(node.left)

        return res