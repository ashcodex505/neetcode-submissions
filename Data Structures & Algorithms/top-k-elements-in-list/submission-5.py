class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kFreq = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            kFreq[n] = 1 + kFreq.get(n, 0)    
        
        for n, c in kFreq.items():
            freq[c].append(n)
        
        res = []

        for num in range(len(freq) - 1, 0, -1):
            for i in freq[num]:
                res.append(i)
                if len(res) == k:
                    return res
            


          

         


