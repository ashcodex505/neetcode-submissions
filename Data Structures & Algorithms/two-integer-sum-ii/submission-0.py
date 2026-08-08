class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        twoSet = {}
        for i ,num in enumerate(numbers):
            diff = target - num 
            if diff in twoSet:
                return [twoSet[diff] + 1,i + 1]
            twoSet[num] = i 
            
