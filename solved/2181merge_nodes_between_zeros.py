# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        interval_toggle = False
        sums = []
        end_list = []
        idx = 0
        while(head.next != None):
            if(head.val == 0):
                interval_toggle = True
                head = head.next
                sums.append(0)
                cur_node = head
                while(interval_toggle == True):
                    if(cur_node.val == 0):
                        idx += 1
                        interval_toggle = False
                        break
                    sums[idx] += cur_node.val
                    if(cur_node.next != None): cur_node = cur_node.next    
            head = head.next
        traverse_node = end_list_head = ListNode(0)
        for node_val in sums:
            traverse_node.next = ListNode(node_val)
            traverse_node = traverse_node.next
        return end_list_head.next
        
            
        