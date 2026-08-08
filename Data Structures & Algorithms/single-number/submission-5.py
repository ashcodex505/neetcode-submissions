class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    
        #hashset way time - O(n) but space is still O(n)
        # seen = set()
        # for n in nums:
        #     if n in seen:
        #         seen.remove(n)
        #     else:
        #         seen.add(n)
        # return list(seen)[0]

        #with bit manipulation we can get space complexity to O(1) 
        #know how to do this so do it tmrw 
        #you use an XOR operaiton for this basically if the two bits are the same say 1 1 = 0 or 0 0 = 0 but if its alternation 1 0 or 0 1 then its equal to 1 
        #so you if you XOR all the integers together you get the integer that is unique out of the entire array 
        res = 0 #space complexity O(1)

        for n in nums:
            res = res ^ n
        return res