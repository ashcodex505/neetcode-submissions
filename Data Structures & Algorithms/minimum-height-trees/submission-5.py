class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # #BRUTE FORCE SOLUTION
        # #first we make our adjacency list by traversing through the list 
        # firstToSecond = defaultdict(list)

        # for f, s in edges:
        #     firstToSecond[f].append(s)
        #     firstToSecond[s].append(f)
        
        # #now we depth first search to traverse our adjanceny list and count the height of each root so we put it in as 
        # #as tuple thats like this (height, root)

        # def dfs(node, parent):
        #     hgt = 0

        #     for nei in firstToSecond[node]:
        #         if nei == parent:
        #             continue #you skip the iteration so you can actuall get through the lop and it isn't infinite
                
        #         hgt = max(hgt, 1 + dfs(nei, node)) #the 1+ will give us the height all the way down 
            
        #     return hgt 



        # minHgt = n 
        # res = [] #to store our roots with min heights 

        # for i in range(n):
        #     currHgt = dfs(i, -1) #-1 bc we're starting the root at i 

        #     if currHgt == minHgt:
        #         res.append(i)
        #     elif currHgt < minHgt:
        #         res = [i]
        #         minHgt = currHgt 
        # return res 

        #EFFICIENT SOLUTION 
        #arlight for the solution we want to first identify leave nodes and then keep popping them and subtractng the n and adding the new leaves until our n <= 2 which we then know that there is a minimum 

           # firstToSecond = defaultdict(list)

        if n == 1:
            return [0]
        firstToSecond = defaultdict(list)
        for f, s in edges:
            firstToSecond[f].append(s)
            firstToSecond[s].append(f)

        
        #now we need to have a count for the number of edges and also add it to our leaves queue 
        leaves = collections.deque()
        cnt = {}
        for f, s in firstToSecond.items(): 
            if len(s) == 1:
                leaves.append(f)
            cnt[f] = len(s)

        #now we have cnt and we have our leaves 
        #now we will go through and find what are the roots with min height which will always be in the middle so we just cnacel out the leave nodes
        while leaves:
            #now our terminating condition 
            if n <= 2:
                return list(leaves) #everything in our leaves queue if its only two will be the center roots of the tree 

            for i in range(len(leaves)): #takes a snapshot of what the leaves are right now 
                node = leaves.popleft()
                n -= 1 #number of nodes has decreased by one 
                for nei in firstToSecond[node]:
                    cnt[nei] -= 1 #basically subtracting 1 from the cnt bc we have now popped a leaf so its neighbors will have one less edge 

                    if cnt[nei] == 1:
                        leaves.append(nei)
            






        
        