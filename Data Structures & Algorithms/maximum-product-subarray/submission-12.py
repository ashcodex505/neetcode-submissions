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
        currMax = 1
        currMin = 1
        for n in nums:
            tmp = n*currMax
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(tmp, n*currMin, n)
            res = max(res, currMax)
        return res
                