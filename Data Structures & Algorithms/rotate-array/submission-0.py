class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return None
        


        for i in range(k):
            num = nums.pop()
            nums.insert(0,num)

 