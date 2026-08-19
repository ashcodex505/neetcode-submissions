"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # so we use depth first search for htis 
        # consturct the wholecrid with quad tree 
        #dfs uses a stack first in last out so it recursively goes down the tree 
        
        #dfs for going through the whole grid once adn seeing if everyhting is the same 

        #double for loop to traverse throuhg grid first for our first four nodes from our root we want to check if the hwole grid is actually the same 
        def dfs(n, r, c): 
            #n is len(grid) and then at start r and c are 0 
            #here we are doing recursive dfs where we start at one point in the grid and go down all the way 
            allSame = True #so one thing that is not the same iwll make this to false 
            #always gooing to be n by n grid 
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break
            #checking edge case right here ^^ 

            #now if we're out here we need to check if allSame si stll true 
            if allSame:
                return Node(grid[r][c], True) #sicne its leaf node we cna implicitly say the children are null 
            
            #base case thats gonna make it stop at a leaf node ^^ 
            #now if we're here we know that we have childrne fro this intenral node 
            n = n // 2 #why ? basically because we are taking the grid into quadrants checking each quadrant and seeing if they're the saem 
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(len(grid), 0, 0) 
        



        
        