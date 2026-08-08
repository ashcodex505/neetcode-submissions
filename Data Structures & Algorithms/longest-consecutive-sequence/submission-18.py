class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        maxVal = 0

        for n in nums:
            count = 1
            cons = n 
            while (cons + 1) in seen:
                count += 1
                cons += 1
            maxVal = max(maxVal, count) 
        return maxVal           