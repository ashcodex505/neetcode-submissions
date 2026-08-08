class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #so for this solution we need to use a hashmap and use a recursive backtracking algorithm that is going to go through every single combination we can 
        #we're going to need to put index i in our backtrack method to keep tracking of what index in the digits string we're at and we are going to have another 
        #paerameter called currString to be able to build our string and so our base case can check if its reached the len of digits 
        

        letterToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        res = []
        if len(digits) == 0: 
            return res
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return #goes and exits the stack and so we can run the rest of the code in the previous stack call 
            
            for c in letterToChar[digits[i]]:
                backtrack(i + 1, currStr + c)
            
        


        backtrack(0, "")
        return res
        


        