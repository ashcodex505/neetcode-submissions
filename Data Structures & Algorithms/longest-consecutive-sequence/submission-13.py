class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        conSet = set(nums)
        longest = 0
        for num in conSet:
            length = 0 
            if (num - 1) not in conSet:
                length += 1
                while (num + length) in conSet:
                    length += 1
                longest = max(longest, length)
        return longest
