class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        twoSum = {}

        for i in range(len(nums)):
            twoSum[nums[i]] = i
        for j in range((len(nums))):
            diff = target - nums[j]
            if diff in twoSum and twoSum[diff] != j:
                return [j, twoSum.get(diff)]

        
      


        