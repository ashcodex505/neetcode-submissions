# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # #traverse throuhg the linked list and put all the numbers in an array and then reverse it and compare 
        # origin = []
        # curr = head
        # while curr:
        #     origin.append(curr.val)
        #     curr = curr.next
        
    

        # return origin[::-1] == origin
        # ##^this is still O(n) time space complexity so lets try doing it in O(1)

        #you would be traversing throuhg hte linked list so you coudld have two pointer going through the list so you could store a numbe 
        #you could traverse linked list one time and get the length of linked list store that in a varailbre 

        #we use a fast point to slow pointer solution to be able to solve this with O(1) time complexity


        #first we set our slow and fast pointers reason being we want to set our slow pointer at the middle of the linked list so that we can then start reversing the second portion of the linked list

        fast, slow = head, head

        while fast and fast.next: #bc we're going doing two .nexts we need to check if both fast and fast.next are not null 
            fast = fast.next.next
            slow = slow.next 
        

        #now slow is at its midpoint and we start reversing the linked list 

        prev = None 
        #^this is what the first .next for slow is going to be pointing to 

        while slow:
            #store slow.next in tmp 
            tmp = slow.next
            slow.next = prev 
            prev = slow #that way this is now the prev value and we can then set slow to tmp 
            slow = tmp 
        

        #now since both are reverse we set both left and right pointer 
        left, right = head, prev 

        while right: #as we can run into the right pointer pointing to null

            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True


            
        