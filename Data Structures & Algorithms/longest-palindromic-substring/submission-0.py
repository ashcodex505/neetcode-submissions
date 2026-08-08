class Solution:
    def longestPalindrome(self, s: str) -> str:
        #max counter to find the longest substring in a string 
        #we need for every substring to reverse that string and then use the == operator to check 
        #requires a two pointer solutoon so we know we need a left and then a right pointer 
        #what are the conditions for moving either the left or the right pointer 
        #gap right now is u dont know hwo left and right pointers work 
        #do this tmrw again to remember realize that you need two while loops one for odd and antoehr for even
        #reason is if u have a string like "ababd" you first take "a" then take "ab" but echeck if theyre equal but u have to do both even and odd or else u wont get longest for stirngs like htis "baab" if u only do odd 
     
        #need to use two while loops 
        #one is going to be for odd and then second is for even 

        res = ""
        maxCount = 0

        #go throuhg every position and use left and right pointers from there 
        for i in range(len(s)):
            #odd 
            l, r = i, i #say if u have string "ababd" the first char is "a" which is odd then we go to even loop which lands on position of "b" where l is at "b" and right is at "a"

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > maxCount:
                    maxCount = (r - l) + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

            #even 
            l, r = i, i+ 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > maxCount:
                    maxCount = (r - l) + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res 


