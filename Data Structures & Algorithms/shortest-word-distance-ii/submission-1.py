class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.strArr = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.strArr[word].append(i)
           

        

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.strArr[word1]
        loc2 = self.strArr[word2] #list of indices 

        i = 0
        j = 0 
        #from start 
        best = float('inf') #just to put a upper limit for when we do min functin 
        while i < len(loc1) and j < len(loc2):
            diff = abs(loc1[i] - loc2[j])
            best = min(best, diff)
            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1
        
        return best
        

        

            
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
