class Solution:
    def reverseBits(self, n: int) -> int:

        num = 31
        tempNum = n
        res = 0

        for i in range(32):
            if tempNum & 1 == 1:
                res += 2**num
            tempNum = tempNum >> 1
            num -= 1
        return res
        
                
        