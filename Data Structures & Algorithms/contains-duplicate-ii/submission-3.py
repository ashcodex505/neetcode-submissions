class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashmap = {}
        # for i, n in enumerate(nums):
        #     if n in hashmap and abs(hashmap[n] - i) <= k:
        #             return True
                
            
        #     else:
        #         hashmap[n] = i 
        # return False

        #solution 2 

        window = set()

        for R in range(len(nums)):


            if R > k:
                window.remove(nums[R-k-1])
            
            if nums[R] in window:
                return True #since already wihtin iwnodw size 
            window.add(nums[R])
        
        return False




        