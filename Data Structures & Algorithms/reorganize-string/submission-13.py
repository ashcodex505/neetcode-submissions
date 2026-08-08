class Solution:
    def reorganizeString(self, s: str) -> str:
        #alrigth so this is the redo of this question
        #so first thing is i put the string in a hasmap and count occurances 
        #then i start putting it in a heap and remember i have to use prev to store the previous 
        count = {}

        for i in s:
            count[i] = count.get(i, 0) + 1
        
        sHeap = []

        for char, num in count.items():
            heapq.heappush_max(sHeap, (num, char))
        
        #okay now for the algorithm

        prev = None 
        res = ""

        while sHeap or prev:
            #if there is nothing in sHeap we know there is an extra char in prev and so we know this canot be pssible 
            if not sHeap:
                return ""
            
            num, char = heapq.heappop_max(sHeap)
            res += char

            num -= 1

            if prev:
                heapq.heappush_max(sHeap, prev)
                prev = None

            if num != 0:
                prev = (num, char)
        
        return res
            

       