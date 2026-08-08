# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #traverse throuhg the linked list and put all the numbers in an array and then reverse it and compare 
        origin = []
        curr = head
        while curr:
            origin.append(curr.val)
            curr = curr.next
        
    

        return origin[::-1] == origin
            
        