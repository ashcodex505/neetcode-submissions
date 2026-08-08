class Solution:
    def isPalindrome(self, x: int) -> bool:
        #this you need to reverse the integer and see but since we have a negative value 
        #how you do it reversing the integer with string operation but lets see without it 
        # original = str(x)
        # reverse = original[::-1]
        # return reverse == original

        #do it without string operation method - and so we use the modulus operator and a division operator. 
        #edge case if number is negative we retunr false 
        if x < 0:
            return False
        
        #we need to find our large to make our div operator so we do a while loop do multiply our div operator to get it to the place of x 
        div = 1
        while x >= (div * 10):
            div *= 10 
        
        while x:
            last = x % 10
            first = x // div 
            if last != first:
                return False
            x = (x % div) // 10
            div = div // 100
        
        

        
        return True

