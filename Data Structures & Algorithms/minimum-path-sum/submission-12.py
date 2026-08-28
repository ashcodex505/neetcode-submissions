from functools import lru_cache 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #m x n grid non-negative numbers 
        #should be able to maximize sum of numbers from left ot right 

        #u baically have a conditon where u are always supposed to end at the bottom right and start at top left only move down or right 

        # rows = len(grid)
        # cols = len(grid[0])
        # min_sum = float("inf")
        # visited = set()

        # @lru_cache(None) #basically cacehs result for functions so if we do the ame call for dfs (#, #) it will already just return that from the caceh we ar just intialziing it ehre 
        # def dfs(r,c):
        #    # Reached bottom-right
        #     if r == rows - 1 and c == cols - 1:
        #         return grid[r][c]

        #     down = dfs(r + 1, c) if r + 1 < rows else float("inf")
        #     right = dfs(r, c + 1) if c + 1 < cols else float("inf")

        #     return grid[r][c] + min(down, right)

        # return dfs(0, 0)

        #dp problem way where you are doing the caching yourself manually 

        rows = len(grid)
        cols = len(grid[0])

        #intialize grid in nx n 

        #memoizing manually through dp right 

        #make a grid where you have one extra column and row and make every entry infinity except for one of the entry on the extra row or column that way what we're going to do is meoize the min paht it takes to get from the entry that we currently looking at to the bottom right entry so we just make every grid entry that so hwen we look for the min entry we've already found it since they're are laready so many subprolbem and we hust solve em all by oging backwards 
        #this grid is going to keep our coutns 
        dpGrid = [ [float("inf")] * (cols + 1) for r in range(rows+1)] #that way with this way we get more rows and cols 

        dpGrid[rows-1][cols] = 0  #when we do first coparison for min path we use this number for min val 

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                dpGrid[r][c] = grid[r][c] + min(dpGrid[r+1][c], dpGrid[r][c+1])
        
        return dpGrid[0][0] 




         


            
     

            
              
        
        


    