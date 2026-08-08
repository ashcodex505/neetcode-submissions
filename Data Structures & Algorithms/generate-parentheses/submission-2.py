class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] #we want to add our paren sequence so we can add it to the res array after we're done exploring a path down the tree
        res = [] #our resutl we are going to return 

        def backtrack(openN, closeN):
            #base case - when openN == closeN == n, meaning you have a sequence of parentheses
            if openN == closeN == n:
                res.append("".join(stack)) #joins all the parens in one string together 
                return 
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN) 
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
            
            







        backtrack(0,0)
        return res


        