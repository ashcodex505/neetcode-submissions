class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute force way 
        output = []
        for i in range(len(nums)):
            ans = 1
            for j in range(len(nums)):
                if j != i:
                    ans *= nums[j]
            output.append(ans)
        return output