class Solution:
    def reverse(self, x: int) -> int:
             
        res = 0
        MIN = -2**31
        MAX = 2**31 - 1

        while x:
            digit = int(math.fmod(x, 10)) #chopped off digit at the end right here 
            x = int(x / 10) #got everything except last digit and reassigned x 

            #now before we add the chopped off digit to our new res integer we need to check whether this is overflwo 
            if((res > (MAX // 10)) or (res == (MAX //10) and digit > int(math.fmod(MAX, 10)))):
                return 0 
            if((res < (MIN // 10)) or (res == MIN // 10 and digit < int(math.fmod(MIN, 10)))):
                return 0 
            res = (res * 10) + digit
        return res            

