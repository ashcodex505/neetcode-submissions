class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #if you put these strs into a hashmap where you basically have <letter, number of occurences> but you aslo need to keep track of position as well 

        #use a hash but also a trie
        #you can also do a screening approach here it is
        i = 0
        length = 100000
        for s in strs:
            length = min(length, len(s))

        res = ""
        while i < length:
            #now we check if every str in strs is the same if so we will add it 
            for s in strs:
                if s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
            i += 1
        
        return res
                
        