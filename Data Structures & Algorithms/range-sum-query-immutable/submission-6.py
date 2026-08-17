class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = (len(nums) + 1) * [0] 
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]
        
        #intiializes them all to zero 
        

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)