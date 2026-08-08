class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs level by level search on this f
        #every level is going to rperesent every minute so every level we finish searching we add a minute to our minute cout n
        #level by level 
        #you have to count all the fresh oranges and then also put all the rotten oranges into your queue 
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0 
        time = 0
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,-1], [1,0], [-1, 0], [0,1]]
        
        while q and fresh > 0:
            
            for i in range(len(q)):
                r, c = q.popleft()


                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1 


       