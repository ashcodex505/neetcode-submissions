# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()

        res = []
        if not root:
            return res
        q.append(root)
   
        while q:
            rightSide = None
            qLen = len(q)
            for i in range(qLen):
                temp = q.popleft()
                if temp:
                    rightSide = temp
                    q.append(temp.left)
                    q.append(temp.right)
            if rightSide:
                res.append(rightSide.val)
          
           

               
                
        return res