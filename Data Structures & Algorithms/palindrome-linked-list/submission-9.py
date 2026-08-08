
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #here we are using a two pointer approach a right and a left pointer and then reversing the second half of the list 

        #first going to set our left and right pointers 
        left, right = head, head 

        while right and right.next:
            right = right.next.next
            left = left.next

        #will put left in the middle 
        #now we reverse the second half 
        prev = None

        curr = left
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp 
        
        #after all of this we are going to set again our left and right pointers of where we are starting from 
        right = prev 
        left = head 

        while right: #reason why is because even after we've gone throuhg hte first half left will point to the next node in the list which will be the midpoint 
            if right.val != left.val:
                return False 
            right = right.next
            left = left.next
        
        return True

       
        