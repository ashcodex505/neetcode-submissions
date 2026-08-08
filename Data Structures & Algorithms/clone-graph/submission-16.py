"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #return deep copy of graph 

        #explore all the node's neighbors and then add it hashmap 
        
        #while disocvring node we also create the nodes for the graph as the values in our hashmap 

        #depth first search in an adjacency list that we are going to create 

        #input node is first node in graph 
        #hashmap oringal ndoe to cloned node 

        preToMap = {}

        def dfs(node): 

            if node in preToMap:
                return preToMap[node]
            
            copy = Node(node.val)

            preToMap[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy 



        return dfs(node) if node else None
        
       

            
       




