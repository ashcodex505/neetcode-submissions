class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = [] #array we're gonna add all fo our strings to 
        #basically using a backtracking solution where we are visting each character and then again revisting it testing every combination we can ahve 
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        if digits == "":
            return res

        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i+1, currStr + c)
        

        backtrack(0,"")
        return res


        