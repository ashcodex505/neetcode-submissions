class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #do this again
        #need to use backtracking to be able to do this 


        rows, cols = len(board), len(board[0])

        pathVisited = set() 


        def dfs(r, c, i):
            #base cases 
            #check if i is equal to length of word since it means we've gone out of bounds for i and we have been able to traverse this path fully 
            if i == len(word):
                return True 

            #check ranges first then check if char is equal to word at i 
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in pathVisited or board[r][c] != word[i]:
                return False
            #that means our position is in range and not in pathVisited set and board[r][c] == word[i]
            #we first add our position to our visited set saying we are exploring this right now and so that we dont visit this same position agian within our path wehn we epxlore 
            pathVisited.add((r,c))
            #here we only need one to be true as that means one of hte paths has found the word 
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)   )

            #then we remove the psoitoon from our visited set so anotehr positon can explroe it 
            pathVisited.remove((r,c))
            
            return res 
        


        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0):
                    return True
        return False