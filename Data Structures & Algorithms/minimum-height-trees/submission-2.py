class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #BRUTE FORCE SOLUTION
        #first we make our adjacency list by traversing through the list 
        firstToSecond = defaultdict(list)

        for f, s in edges:
            firstToSecond[f].append(s)
            firstToSecond[s].append(f)
        
        #now we depth first search to traverse our adjanceny list and count the height of each root so we put it in as 
        #as tuple thats like this (height, root)

        def dfs(node, parent):
            hgt = 0

            for nei in firstToSecond[node]:
                if nei == parent:
                    continue #you skip the iteration so you can actuall get through the lop and it isn't infinite
                
                hgt = max(hgt, 1 + dfs(nei, node)) #the 1+ will give us the height all the way down 
            
            return hgt 



        minHgt = n 
        res = [] #to store our roots with min heights 

        for i in range(n):
            currHgt = dfs(i, -1) #-1 bc we're starting the root at i 

            if currHgt == minHgt:
                res.append(i)
            elif currHgt < minHgt:
                res = [i]
                minHgt = currHgt 
        return res 



        

        