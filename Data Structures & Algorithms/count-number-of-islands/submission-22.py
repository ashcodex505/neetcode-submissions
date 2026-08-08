class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                visited.add((row,col))
                directions = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col -1)]
                for dr, dc in directions:
                    if (dr, dc) not in visited and dr in range(len(grid)) and dc in range(len(grid[0])) and grid[dr][dc] == "1":
                        q.append((dr,dc)) 




            






        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands




