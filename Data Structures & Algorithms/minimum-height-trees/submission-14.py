class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

            # #brute force way is really going through every node and so our time complexity for this is going to O(n^2)

            # #we need to make an adj list here
            # adjList = defaultdict(list)



            # for u, v in edges:
            #     adjList[u].append(v)
            #     adjList[v].append(u)
            


            # def dfs(node, parent):
            #     currHeight = 0
            #     for i in adjList[node]:
            #         if i == parent:
            #             continue
                    
            #         currHeight = max(currHeight, 1 + dfs(i, node))
            #     return currHeight
                
                




            # minHeight = n
            # res = [] #going to be our array here 

            # for i in range(n):
            #     curHeight = dfs(i, -1) #first param is the node n and the second is going to be -1 since we are starting from the root and this is going throuhg every node labeled 0 to n-1  

            #     if curHeight < minHeight:
            #         res = [i]
            #         minHeight = curHeight
            #     elif curHeight == minHeight:
            #         res.append(i)
            
            # return res 
            #efficient way to do this problem

            #wer'e going to start with the leaves so the outermost layer then we are slowly gonna pop each leaf and assign new leaves until we get to about n <= 2 nodes then we know we have our nodes 
                  # adjList = defaultdict(list)

            adjList = defaultdict(list)

            for u, v in edges:
                adjList[u].append(v)
                adjList[v].append(u)

            #count hashmap for number of leaves 
            leaves = collections.deque() #store leaf nodes here
            count = {} #counts how mnay edges a node has
             
            for i in range(n):
                count[i] = len(adjList[i])
                if count[i] == 1:
                    leaves.append(i)
                
            if n == 1:
                return [0]
            while leaves: 
                if n <= 2:
                    return list(leaves) #because our leaves will have the root node which will either be two or 1 always 

                for i in range(len(leaves)):
                    node = leaves.popleft()
                    #now we check if the neighbor of this node had any other neighbors 
                    n -= 1
                    for nei in adjList[node]:
                        count[nei] -= 1
                        if count[nei] == 1:
                            leaves.append(nei)
                        
                    








        
        