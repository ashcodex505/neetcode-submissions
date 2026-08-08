# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #creating a new listnode that will point to the head and then we are having 
        #a left and right pointer that have a "n" number of seperation between them \
        #when the right pointer gets to the Null node then whatever the left pointer is on we 
        #switch the links to skip the node the left point pointre is on 
        dummy = ListNode(0, head)
        currentLeft = dummy
        currentRight = head
      
        for i in range(n):
                currentRight = currentRight.next
        while currentRight:
            
            currentLeft = currentLeft.next
    
            
            currentRight = currentRight.next
       
        
        currentLeft.next = currentLeft.next.next
        return dummy.next   

            
        
            

