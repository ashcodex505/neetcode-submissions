class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #inefficient way but still did it by yourself 

        # longest = 0
        
        
        # for i in range(len(s)):
        #     length = 0
        #     repeat = {}
        #     while i + length < len(s) and s[i + length] not in repeat:
        #         repeat[s[i+length]] = i + length
        #         length += 1
              

        #     longest = max(longest, length)
        # return longest 


        #efficient way 

        #you're going to use a set here to basically identify any duplicates you have 
        charSet = set()
        res = 0
        #set your left pointer to 0 as this one will only increment if we find a duplicate val 
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res




            