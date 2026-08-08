class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            topK[n] = topK.get(n, 0) + 1
        for n, c in topK.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

         


