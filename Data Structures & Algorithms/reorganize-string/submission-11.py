class Solution:
    def reorganizeString(self, s: str) -> str:
        #reorganize the string 
        #first thing we need to do is indentify what strings are adjacent to each other 

        #so one thing we can do is just count the ocurrances of the characters in the string 
        #put string in hashmap first to count occurances 
        countOfChars = {}
        for i in s:
            countOfChars[i] = countOfChars.get(i, 0) + 1
     

        
        #now we are going to have a heap where we push a tuple (numOfoccurance, char) ever time we pop it out if the numOfOccurences - 1 does not equal 0 then we push (n-1, char) back in the heap 
        #now we need to also return "" if this is not possible 
        sHeap = []

        for char, num in countOfChars.items():
            heapq.heappush_max(sHeap, (num, char))
        #now everything is in the heap so now we basically add chars to our string 
        res = ""
        prev = None #will store our previous 
        while sHeap or prev:
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
                
            
            
        
 
            




        