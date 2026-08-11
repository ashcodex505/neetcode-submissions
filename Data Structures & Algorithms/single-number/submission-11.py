class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       #O(n) time and O(1) run 

       #they use xor operation to be able to do this 

        results = 0 
       # any number xor with 0 is just gonna be itself and xor is inherently has a property of bieng ocmmunicative and assoiative 
#xor operation is ^= 
        for n in nums: 
            results ^= n 
        
        return results