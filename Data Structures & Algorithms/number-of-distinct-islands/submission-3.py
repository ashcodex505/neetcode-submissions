class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        #for this you need to store the shape of the path you are taking for each island 

        #so first we will have two set and one of the set will be used to store our shapes and so if u have any duplicte tuples that will not be added and then we can take the length of this set to find the number of distinct islands 
        visited = set() 
        directUnique = set()

        def dfs(r, c, direction):  #need to have direction as that will be within our path
            #check with if statements 

            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or (r,c) in visited or grid[r][c] == 0:
                return 
            
            visited.add((r,c))
            #put in your set so now you dont revisit that island again 
            directionsList.append(direction) #we append this to our list to track how we moved 
            dfs(r+1, c, "D")
            dfs(r-1, c, "U")
            dfs(r, c+1, "R")
            dfs(r, c-1, "L")
            directionsList.append("0") #we do this to make it distinct as some shapes could be regarded the same if we dont do this as when we go up the stack we need to track that and this is the way we do that 




        for r in range(len(grid)):
            for c in range(len(grid[0])):
                directionsList = []

                #and so we are now going to be starting off 
                dfs(r, c, "0")
                if directionsList:
                    directUnique.add(tuple(directionsList)) #making the list of directions for one island path added to this set as a tuple as that is hashable 
        
        return len(directUnique) 

        