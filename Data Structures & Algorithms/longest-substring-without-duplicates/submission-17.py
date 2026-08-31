class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #to use the ord function to be able to know that it continguous right so we its 1 different of each charater postive 1 
        #piitner solution - left and right pinter our left is goingto be start of sequ while our right is going to the current character we are on 
        #come bakc to this 
        # #stick to this 
        charSet = set()
        l = 0 
        r = 0

        count = 0
        while r < len(s):
            if s[r] in charSet:
                count = max(count, (r-l))
                charSet.remove(s[l])
                
                l += 1
                continue 

            if s[r] not in charSet:

                charSet.add(s[r])
                r += 1 
                count = max(count, r - l)
        return count 


            
   



            