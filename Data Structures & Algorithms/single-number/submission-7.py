class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #take a hashmap and count every instance of the number but at the end of couting each instance of number we reverse key and values and then return the value that has an instance of 1 as the answer 

        num_map = {}

        for n in nums:
            num_map[n] = num_map.get(n, 0) + 1 
        

        for num, count in num_map.items():
            if count == 1: 
                return num 


     