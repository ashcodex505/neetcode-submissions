class Solution:
    def countBits(self, n: int) -> List[int]:
        #brute force where O(nlogn)
        # res = [0] * (n+1)
        # for i in range(1, n+1):
        #     num = i 
        #     while num != 0:
        #         res[i] += 1 
        #         num &= (num - 1)
        # return res 
        ###############################

        #brute froce my way 

        res = []

        for i in range(n+1):
            count = 0
            while i > 0:
                if i & 1 == 1:
                    count += 1
                i = i >> 1
            res.append(count)
        return res
   
