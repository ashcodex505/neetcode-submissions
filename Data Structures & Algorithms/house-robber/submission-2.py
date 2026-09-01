class Solution:
    def rob(self, nums: List[int]) -> int:
        #know solution do it tmrw 

        #we're doing it 
        #two rob1 and rob2 pointers where rob1 stores the sum of two houses back and rob1 sotres the max sum from one house back 
        rob1, rob2 = 0, 0 
       
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2 
            rob2 = temp 
        return rob2 
