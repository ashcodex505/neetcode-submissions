class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #you cant do a one pass bc you wont be able to find the max subarr
        #my approach is going to be with left and right pointer 
        #or we can do a slow and fast pointer solution 
        curSum = nums[0] #tracks sum of the elements this is going to be our running sum 
        #do this tmrw when you forget 

        #so we're going to go through each element in nums and if the sum itself inside is negative then we reset to 0 
        res = 0

        for n in nums:
            if res < 0:
                res = 0
            res += n
            curSum = max(res, curSum)

        return curSum

        