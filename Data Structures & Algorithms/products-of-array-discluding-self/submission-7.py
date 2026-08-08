class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #double for loop 
        res = []
        for n in range(len(nums)): 
            num = 1;
            for j in range(len(nums)):
                if(j != n):
                    num = num * nums[j]
            res.append(num)
        return res

        #whats the efficient way? 
