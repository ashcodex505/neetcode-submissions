class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we use hashmap to be able to know count of each 
        #two hashmaps one for s and another for t 
        if not len(s) == len(t):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
        for j in range(len(t)):
            tMap[t[j]] = 1 + tMap.get(t[j], 0)
        
        for n in range(len(s)):
            if not (s[n] in tMap and sMap[s[n]] == tMap[s[n]]) or not (t[n] in sMap and tMap[t[n]] == sMap[t[n]]):
                return False
        return True
            

        
      

#Two dictionaries are considered equal if and only if they meet two conditions:

# They have the exact same set of keys.

# The value associated with each key is the same in both dictionaries.


        

        