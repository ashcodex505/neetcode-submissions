class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #you would use a maxheap and have tuples (weight, index) in it so it'll pop out the max weight from the heap and you can keep pushing in the heap 
        #how to implement a maxheap - you use negative values rather than positve and then switch them to positive value 
    
        maxHeap = []

        for index, val in enumerate(stones):
            heapq.heappush(maxHeap, -val)


        while len(maxHeap) > 1:
            val1 = heapq.heappop(maxHeap)
            val2 = heapq.heappop(maxHeap)
            if (-val1) > (-val2):
                newVal1 = (-val1) - (-val2)
                heapq.heappush(maxHeap, -newVal1)
                
            elif (-val1) < (-val2):
                newVal2 = (-val2) - (-val1)
               
                heapq.heappush(maxHeap, -newVal2)
           
        return -maxHeap[0] if len(maxHeap) == 1 else 0


            