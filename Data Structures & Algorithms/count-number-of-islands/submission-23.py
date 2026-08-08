class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        # islands = 0
        # visited = set()
        # def bfs(r,c):
        #     q = collections.deque()
        #     q.append((r,c))
        #     while q:
        #         row, col = q.popleft()
        #         visited.add((row,col))
        #         directions = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col -1)]
        #         for dr, dc in directions:
        #             if (dr, dc) not in visited and dr in range(len(grid)) and dc in range(len(grid[0])) and grid[dr][dc] == "1":
        #                 q.append((dr,dc)) 




            






        # rows = len(grid)
        # cols = len(grid[0])

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visited:
        #             bfs(r,c)
        #             islands += 1
        # return islands

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            # out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            # water or already visited
            if grid[r][c] == "0" or (r, c) in visited:
                return

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands



