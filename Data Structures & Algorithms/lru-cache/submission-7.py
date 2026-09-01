class Node:
    def __init__(self, key, value):
        self.key = key 
        self.val = value 
        self.prev = None 
        self.next = None     



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        #when we intialzier this cache we need two nodes that rpesent left and right left being lru rigth being mru 

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right 
        self.right.prev = self.left
        self.lruMap = {} #map a key to a node pointer 
    
    def append(self, node): #adding the node to the linked list 

        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node 
        self.right.prev = node 

    

    def remove(self, node): #just taking the node out of the linkedlist   

        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key in self.lruMap: 
            self.remove(self.lruMap[key]) 
            self.append(self.lruMap[key])

            return self.lruMap[key].val
        return -1  #not found 
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.lruMap:
            self.lruMap[key].val = value 
            self.remove(self.lruMap[key])
            self.append(self.lruMap[key])
        else:
            node = Node(key,value)
            self.lruMap[key] = node 
            self.append(self.lruMap[key])
        
        if len(self.lruMap) > self.capacity:
            #we take out the node in the left of linked lsit 
            tempkey = self.left.next.key
            self.remove(self.left.next)
            del self.lruMap[tempkey]
        
            
