class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #lets create a hashmap
        count = {} #key : number value: number of occurences 
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for k, v in count.items():
            if v > (len(nums) // 2):
                return k
        

        
        