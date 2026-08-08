class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # #lets create a hashmap
        # count = {} #key : number value: number of occurences 
        # for n in nums:
        #     count[n] = count.get(n, 0) + 1
        
        # for k, v in count.items():
        #     if v > (len(nums) // 2):
        #         return k

        #efficient way of solving this 
        #solve this later at the end of the night 

        #we use the boyer voiting algo to oslve this in O(1) space complexity 
        candidate = 0
        count = 0 

        for n in nums:
            if count == 0:
                candidate = n 
                
            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate 




        

        
        