class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countNums = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in countNums:
                return [countNums[diff], i]
            countNums[n] = i
      
