# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #put all the nodes through a bfs algo in a queue and at the end we check the right most value as that's going to be the node we on the righ side 
        q = collections.deque()

        res = []

        q.append(root)
        while q:
            qLen = len(q)
            rightNode = None

            for i in range(qLen):
                node = q.popleft()
                
                #bfs algo 
                #level by level
                if node: #i remembered this
                    rightNode = node 
                    q.append(node.left)
                    q.append(node.right)
            if rightNode:
                res.append(rightNode.val)
        return res
                