

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force way
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):  # Start j from i+1
        #         if nums[j] == nums[i]:
        #             return True
        # return False

        #hash set way with time complexity of O(n)
        mySet = set()
        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)
        return False
