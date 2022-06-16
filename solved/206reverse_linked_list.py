from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        
        tail = head
        stack = deque()
        while(tail != None):
            stack.appendleft(tail)
            tail = tail.next
        
        head = stack.popleft()
        tail = ListNode()
        head.next = tail
        while len(stack) > 0:
            tail.val = stack.popleft().val
            if(len(stack) > 0): 
                tail.next = stack[0]
                tail = tail.next
            else:
                tail.next = None
                break
        return head
            