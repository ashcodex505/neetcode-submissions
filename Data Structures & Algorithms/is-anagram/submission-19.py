class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # #efficient way  Time compexity of O(n + m) and space complexiry O(n + m)

        # sMap = {}

        # tMap = {}

        # for i in s:
        #     sMap[i] = sMap.get(i, 0) + 1
        
        # for j in t:
        #     tMap[j] = tMap.get(j, 0) + 1

        # return tMap == sMap  

        #anotehr way sorted way 

        #first we check lenght 
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)      


        


        