class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list) #hashmap with value eing defaults to arrays

        # array for len 26 and put in a set each array  
        for s in strs:
            
            char = [0] * 26
            for i in s: 
                char[ord(i) - ord("a")] += 1 
            

            char = tuple(char)
            
            strMap[char].append(s)
     
     
        
        return list(strMap.values())

        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())






