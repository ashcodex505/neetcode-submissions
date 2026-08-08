class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
       if not grid:
            return 0
       islands = 0
       cols = len(grid[0])
       rows = len(grid)
       isVisited = set()
       def bfs(row, col):
            queue = collections.deque()
            isVisited.add((row,col))
            queue.append((row,col))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if(r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in isVisited):
                        queue.append((r,c))
                        isVisited.add((r,c))
                    

        
       
       for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in isVisited:
                    bfs(r,c)
                    islands += 1
       return islands

       