class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hashmap and ascii values 
        res = defaultdict(list) #allows to create an empty list basically 
        #go through your entire array 
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()





        