# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #returning true if there is at least one node that can be visited again (2 times) by the .next pointer 
        #the index determined beginning of cycle
        #hashmap -> keys: nodes, values: index 
        nodeMap = {}

        curr = head
        index = 0
        while curr:
            if curr in nodeMap:
                return True
            nodeMap[curr] = index
            index += 1
            curr = curr.next
        return False


        