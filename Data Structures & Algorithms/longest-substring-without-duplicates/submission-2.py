class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        
        for i in range(len(s)):
            length = 0
            repeat = {}
            while i + length < len(s) and s[i + length] not in repeat:
                repeat[s[i+length]] = i + length
                length += 1
              

            longest = max(longest, length)
        return longest 



            