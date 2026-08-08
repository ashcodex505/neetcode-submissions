# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count1 = 0 
        curr = head 
        while curr != None: 
            count1 += 1 
            curr = curr.next
        
        mid = int(count1 // 2)
        count2 = -1
        curr1 = head
        while count2 != mid:
            count2 += 1
            if count2 != 0:
                curr1 = curr1.next
        
        return curr1




        