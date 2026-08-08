class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #we need a maxHeap so that we get the two largest stones 
        if len(stones) == 0 or stones == None:
            return 0
        
        mHeap = []

        for val in stones:
            heapq.heappush(mHeap, -val)
        while len(mHeap) > 1:
            val1 = -heapq.heappop(mHeap)
            val2 = -heapq.heappop(mHeap)
            if val1 > val2:
                newVal1 = val1 - val2
                heapq.heappush(mHeap, -newVal1)
            elif val1 < val2:
                newVal2 = val2 - val1
                heapq.heappush(mHeap, -newVal2)
            
        return -mHeap[0] if len(mHeap) == 1 else 0


            