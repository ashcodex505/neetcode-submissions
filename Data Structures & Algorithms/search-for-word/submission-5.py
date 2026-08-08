class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #this going to use matrix depth first search so its going ot be harder 
        #so here we are using backtracing to be able to do this meaning its very inefficent and so we are removing the state which state being the visited set 
        rows, cols = len(board), len(board[0])

        pathVisited = set() #going to be our positions that we visited so far in our path but we need to remove after we are done with searching each position in dpeth 

        def dfs(r, c, i):

            #checking if i is equal to length of word if so we've found the word in the grid so we return true 
            if i == len(word):
                return True 
            
            #now we check for all the invalidation as we want to be able to return false if one of these conditions are true 

            if r < 0 or c < 0 or (r,c) in pathVisited or r >= rows or c >= cols or board[r][c] != word[i] :
                return False
            
            #if both of the if statements are not true then we do our recurive call to depth first search in left right up and down directions and also we know that sequence is stlll right for the word 

            #so we ware going to have a variable called res that i going to store a boolean value basically if one of the calls to dfs returns treu then it will go all the way up the stack and then if all fo them are false we return false here as well
            #
            pathVisited.add((r,c))
            res = (dfs(r+1, c, i+1) or 
                    dfs(r-1, c, i+ 1) or 
                    dfs(r, c+1, i+ 1) or 
                    dfs(r, c -1, i+ 1) 
            )
            pathVisited.remove((r,c))
            return res 




        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0): 
                    return True 
        return False 


