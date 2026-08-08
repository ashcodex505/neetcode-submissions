class Solution:
    def isPalindrome(self, x: int) -> bool:
        #this you need to reverse the integer and see but since we have a negative value 
        original = str(x)
        reverse = original[::-1]
        return reverse == original