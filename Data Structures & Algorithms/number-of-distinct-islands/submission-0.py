class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        #so for this one instead of storing absolute coordinates we are instead storing path taken during dfs and os path becomes a shape signature 

        def dfs(row,col, direction):
            if row < 0 or col < 0 or row>= len(grid) or col >= len(grid[0]):
                return
            if (row,col) in seen or grid[row][col] == 0:
                return
            seen.add((row,col)) #we are marking this as visited before we do our depth first search
            path_signature.append(direction) #recording direction in our list 
            dfs(row + 1, col, "D")
            dfs(row - 1, col, "U")
            dfs(row, col + 1, "R")
            dfs(row, col - 1, "L")
            path_signature.append("0") #need to ahve this so we can record the backtracking and say we're done exploring this position and we go up the stack trace 
            #^^ we need this because we need to record our path as when we are going up our stack traces thats also directions we're going in and so without this our algo is not goign to find uniqeu paths 



        
        seen = set() #visited cells 
        unique_islands = set() #sotring unique shapes, we store directions and so when we have a tuples that we add in here that is the same direction it isn't added in again as its not unique 

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                path_signature = [] #this is going to store records of how we moved to reach a cell 
                dfs(row,col, "0") #the zero marks oru starting point of the cells we are gonig to explore 
                if path_signature:
                    unique_islands.add(tuple(path_signature)) #our list is changed to a tuple as tuples are hashable and sets require hashable types as lists arent hashable 
        return len(unique_islands)




                    