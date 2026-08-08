class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

          #brute force solution 

            #go throuhg every node

            adjList = defaultdict(list)
            
            for u, v in edges:
                adjList[u].append(v)
                adjList[v].append(u)
            




            def dfs(node, parent):
                currHeight = 0
                
                for nei in adjList[node]:
                    if nei == parent:
                        continue 
                    
                    currHeight = max(currHeight, 1 + dfs(nei, node))
                
                return currHeight 

                

            minHeight = n
            res = []
            for i in range(n):
                currHeight = dfs(i, - 1)
                
                if currHeight < minHeight:
                    res = [i]
                    minHeight = currHeight 
                elif currHeight == minHeight:
                    res.append(i)
                
            return res 

            



                        
                    








        
        