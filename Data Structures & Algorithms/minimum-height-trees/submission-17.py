class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        #   #brute force solution 

        #     #go throuhg every node

        #     adjList = defaultdict(list)
            
        #     for u, v in edges:
        #         adjList[u].append(v)
        #         adjList[v].append(u)
            




        #     def dfs(node, parent):
        #         currHeight = 0
                
        #         for nei in adjList[node]:
        #             if nei == parent:
        #                 continue 
                    
        #             currHeight = max(currHeight, 1 + dfs(nei, node))
                
        #         return currHeight 

                

        #     minHeight = n
        #     res = []
        #     for i in range(n):
        #         currHeight = dfs(i, - 1)
                
        #         if currHeight < minHeight:
        #             res = [i]
        #             minHeight = currHeight 
        #         elif currHeight == minHeight:
        #             res.append(i)
                
        #     return res 


        #efficient solution - we start with leaves first 

        adjList = defaultdict(list)
        
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        

        count = {}
        leaves = collections.deque()

        for i in range(n):
            count[i] = len(adjList[i])
            if count[i] == 1:
                leaves.append(i)
        
        #we have stored the counts 
        if n == 1:
            return [0]

        while leaves:
            if n <= 2:
                return list(leaves)
            
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adjList[node]: #all the neighbors for the node you just popped you need to decrease those neighbor nodes by one 
                    count[nei] -= 1
                    if count[nei] == 1:
                        leaves.append(nei)   
                     



                        
                    








        
        