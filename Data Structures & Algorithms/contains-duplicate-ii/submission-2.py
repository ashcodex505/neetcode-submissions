class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        count = 0
        for i, n in enumerate(nums):
            if n in hashmap and abs(hashmap[n] - i) <= k:
                    return True
                
            
            else:
                hashmap[n] = i 
        return False

        