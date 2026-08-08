class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kElements = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            kElements[num] = 1 + kElements.get(num, 0)
        for num, cnt in kElements.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1 , 0, -1 ):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    


        