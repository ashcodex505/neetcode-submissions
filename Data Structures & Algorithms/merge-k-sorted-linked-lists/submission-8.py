# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        # minHeap = []
        # root = ListNode()
        # curr = root

        # # Edge case: Empty input list
        # if not lists:
        #     return None  # Fixed incorrect return

        # # Push all list heads into the heap
        # for l in lists:
        #     while l:  # Fixed `while l.next != None`
        #         heapq.heappush(minHeap, (l.val, id(l), l))  # Use id(l) to avoid tuple comparison issue
        #         l = l.next  

        # # Extract from heap and build sorted list
        # while minHeap:  # Fixed incorrect for loop
        #     val, _, node = heapq.heappop(minHeap)
        #     curr.next = node
        #     curr = node
        #     curr.next = None  # Prevent cycles by cutting old links

        # return root.next  # Fixed return to skip dummy node


        # the linked lists way 
        if not lists or len(lists) == 0:
            return None 
        while len(lists) > 1:
            mergeLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None 
                mergeLists.append(self.mergeList(l1, l2))
            lists = mergeLists
        return lists[0]


    def mergeList(self, l1, l2):
        dummyNode = ListNode()
        curr = dummyNode
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1 
          
                l1 = l1.next
            else:
                curr.next = l2
          
                l2 = l2.next 
            curr = curr.next
        if l1:
            curr.next = l1
        if l2: 
            curr.next = l2 
        return dummyNode.next 
                
            


                    
