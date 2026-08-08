class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        s_Map = {}
        t_Map = {}
        for i in s: 
            s_Map[i] = s_Map.get(i, 0) + 1
        for j in t:
            t_Map[j] = t_Map.get(j, 0) + 1
        print(s_Map)
        print(t_Map)
        return s_Map == t_Map

        

        