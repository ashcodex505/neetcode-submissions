class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

            #brute force way is really going through every node and so our time complexity for this is going to O(n^2)

            #we need to make an adj list here
            adjList = defaultdict(list)



            for u, v in edges:
                adjList[u].append(v)
                adjList[v].append(u)
            


            def dfs(node, parent):
                currHeight = 0
                for i in adjList[node]:
                    if i == parent:
                        continue
                    
                    currHeight = max(currHeight, 1 + dfs(i, node))
                return currHeight
                
                




            minHeight = n
            res = [] #going to be our array here 

            for i in range(n):
                curHeight = dfs(i, -1) #first param is the node n and the second is going to be -1 since we are starting from the root and this is going throuhg every node labeled 0 to n-1  

                if curHeight < minHeight:
                    res = [i]
                    minHeight = curHeight
                elif curHeight == minHeight:
                    res.append(i)
            
            return res 




        
        