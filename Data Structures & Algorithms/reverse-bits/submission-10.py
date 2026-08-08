class Solution:
    def reverseBits(self, n: int) -> int:
        #& bit operation to be able to identify if the number is 1 or 0 and then based on that make our number and shift to the right 
        number = 31
        res = 0
        

        for i in range(32):
            if n & 1 == 1:
                res += 2**number
            n = n >> 1
            number -= 1
        return res