# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        to_eval = []
        node = head
        while(node != None):
            to_eval.append(node.val)
            node = node.next
        if(str(to_eval[::-1]) == str(to_eval)):
            return True
        else:
            return False

    # Worse solution, adapted from discussion. O(N) + O(1)
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     to_eval = []
    #     node = head
    #     while(node != None):
    #         to_eval.append(node.val)
    #         node = node.next
        
    #     # Iterate from start and from end to MIDDLE
    #     # (first condition), AND checking if elements are equal
    #     start_idx, end_idx = 0, len(to_eval) - 1
        
    #     while(start_idx <= end_idx and to_eval[start_idx] == to_eval[end_idx]):
    #         start_idx += 1
    #         end_idx -= 1
        
    #     if(start_idx > end_idx):
    #         return True
    #     else:
    #         return False