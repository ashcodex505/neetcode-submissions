class Solution:
    def rob(self, nums: List[int]) -> int:


        #now we need to do this but noow hosues are in a circle 

        #we just call house robber 1 and only do it on the array everything from the 0 to second to last and do that backwards too
        if len(nums) == 1:
            return nums[0]

        def rob1(houses):
            rob1, rob2 = 0 ,0
            for n in houses:
                temp = max(rob1 + n , rob2)
                rob1 = rob2 
                rob2 = temp 
            
            return rob2 

        
        return max(rob1(nums[0:len(nums)-1]), rob1(nums[len(nums)-1: 0: -1]))


        
        