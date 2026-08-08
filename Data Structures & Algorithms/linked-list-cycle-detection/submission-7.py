# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = set()
        curr = head 
        while curr:
            print(curr.val)
            if (curr.val in cycle):
                return True
            cycle.add(curr.val)
            curr = curr.next
        print(cycle)
        return False


        