class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        #building the hashmap 
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        #checking hashmap with other one 
        for t in countT:
            if countT[t] != countS.get(t, 0):
                return False
        return True 
        
                
        
        