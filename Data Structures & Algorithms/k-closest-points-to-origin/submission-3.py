class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we use heaps to store distance output 
        #we use that distance formula for two points from origin to the first array and then push that distance output into a minheap store into minheap as tuple (double d, [int x, int y])
        #so then after we use a for loop to pop out the k points from minheap so we get the array 
        res = []
        for point in points:
            dist = math.sqrt(math.pow(point[0] - 0, 2) + math.pow(point[1] - 0, 2))
            heapq.heappush(res, (dist, point))
        finalPoint = []
        for i in range(k):
            dist, point = heapq.heappop(res)
            finalPoint.append(point)
    
        return finalPoint
