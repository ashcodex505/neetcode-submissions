class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #I assumed it was two but this works for two 
        # adjList ={}
        # maxProd = -100000
        # for n in nums:
        #     adjList[n] = None 
        # for i in range(len(nums)):
        #     if nums[i] in adjList:
        #         if (i+1) < len(nums):
        #             adjList[nums[i]] = nums[i+1]
        #             maxProd = max(maxProd, nums[i+1] * nums[i])
        #         else:
        #             maxProd = max(maxProd, nums[i])
        # return maxProd

        #how to do it for more than two 
        res = nums[0]
        curMin, curMax = 1, 1 #reason why is because you want it to still be like this even if you reset
        for n in nums: 
            
            tmp = curMax * n 
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin* n, n)
            res = max(res, curMax)
        return res
            
                