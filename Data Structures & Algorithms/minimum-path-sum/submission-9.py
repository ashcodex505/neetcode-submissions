from functools import lru_cache 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #m x n grid non-negative numbers 
        #should be able to maximize sum of numbers from left ot right 

        #u baically have a conditon where u are always supposed to end at the bottom right and start at top left only move down or right 

        rows = len(grid)
        cols = len(grid[0])
        min_sum = float("inf")
        visited = set()

        @lru_cache(None)
        def dfs(r,c):
           # Reached bottom-right
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]

            down = dfs(r + 1, c) if r + 1 < rows else float("inf")
            right = dfs(r, c + 1) if c + 1 < cols else float("inf")

            return grid[r][c] + min(down, right)

        return dfs(0, 0)
            
     

            
              
        
        


    