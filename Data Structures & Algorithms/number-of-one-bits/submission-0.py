class Solution:
    def hammingWeight(self, n: int) -> int:
        #you've done this before 
        #we use the bit operation & again here 

        res = 0
        for i in range(32):
            if n & 1 == 1:
                res += 1
            n = n >> 1
        return res