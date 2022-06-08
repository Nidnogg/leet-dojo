# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while(node != None):
            if(node.next):
                if(node.next.val == node.val):
                    node.next = node.next.next
                    continue
            node = node.next
        return head
                
        