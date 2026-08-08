class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #brute force way
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return False
        #efficient way with less time complexity 
        myHash = {}
        for i in range(len(nums)):
            if (target - nums[i]) in myHash:
                return [myHash[target-nums[i]], i]
            else:
                myHash[nums[i]] = i

        #using enumerate through same thing but different python for loop
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            return 

            


        