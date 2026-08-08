class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        twoSet = defaultdict(list)
        res = []
        nums.sort()
        
        
        for i, num in enumerate(nums):

            if i and nums[i] == nums[i-1]:
                continue
            l ,r = i+1, len(nums) -1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
            
            

