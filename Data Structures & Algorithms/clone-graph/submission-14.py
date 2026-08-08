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
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy 

            for nei in node.neighbors:
                oldToNew[node].neighbors.append(clone(nei))
            return copy



        return clone(node) if node else None

            
       




