class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False  # If we can't reach this index, return False
            max_reach = max(max_reach, i + nums[i])  # Update the farthest index we can reach
            if max_reach >= len(nums) - 1:
                return True  # If we can reach or surpass the last index, return True
        return False
        