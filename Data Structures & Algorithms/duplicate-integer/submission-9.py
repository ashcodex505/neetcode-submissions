class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        #the other way you were trying to do 
        # dup = {} # Initialize an empty dictionary (hash map)
        
        # # First, count the occurrences of each number
        # for num in nums:
        #     dup[num] = dup.get(num, 0) + 1
            
        # # Now, check if any number appeared more than once
        # for count in dup.values():
        #     if count > 1:
        #         return True # Found a duplicate count
                
        # return False # No counts were greater than 1
        

        