class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute force way 
        # output = []
        # for i in range(len(nums)):
        #     ans = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             ans *= nums[j]
        #     output.append(ans)
        # return output
        #O(n)
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res

        