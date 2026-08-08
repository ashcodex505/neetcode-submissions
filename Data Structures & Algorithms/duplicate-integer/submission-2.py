

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force way
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Start j from i+1
                if nums[j] == nums[i]:
                    return True
        return False
