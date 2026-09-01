class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        def rob1(nums2):
            rob1, rob2 = 0, 0 #pinters fro both one house back and two houses back 

            for n in nums2:
                temp = max(rob1 + n, rob2)
                rob1 = rob2 
                rob2 = temp 
            
            return rob2 



        return max(rob1(nums[len(nums)-1:0:-1]), rob1(nums[0:len(nums)-1]))
        