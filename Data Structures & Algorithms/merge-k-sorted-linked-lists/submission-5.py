# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        minHeap = []
        root = ListNode()
        curr = root

        # Edge case: Empty input list
        if not lists:
            return None  # Fixed incorrect return

        # Push all list heads into the heap
        for l in lists:
            while l:  # Fixed `while l.next != None`
                heapq.heappush(minHeap, (l.val, id(l), l))  # Use id(l) to avoid tuple comparison issue
                l = l.next  

        # Extract from heap and build sorted list
        while minHeap:  # Fixed incorrect for loop
            val, _, node = heapq.heappop(minHeap)
            curr.next = node
            curr = node
            curr.next = None  # Prevent cycles by cutting old links

        return root.next  # Fixed return to skip dummy node
                    
