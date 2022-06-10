# Terrible runtime (13%), good memory. (40%)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        head_l3 = l3
        l1_str = ""
        l2_str = ""
        while(l1 != None):
            l1_str += str(l1.val)
            l1 = l1.next
        while(l2 != None):
            l2_str += str(l2.val)
            l2 = l2.next
        sum = int(l1_str[::-1]) + int(l2_str[::-1])
        while sum != 0:
            l3.val = sum % 10
            sum = sum // 10
            print(l3.val)
            if(sum == 0): break
            l3.next = ListNode()
            l3 = l3.next
        return head_l3
        
            
# Second WIP Solution      
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         l3 = ListNode()
#         head_l3 = l3
#         carry = 0
#         while(True):
#             if(l1 != None and l2 != None):
#                 carry = (l1.val + l2.val + l3.val) // 10
#                 l3.val = (l1.val + l2.val + l3.val) % 10  
#                 l1 = l1.next
#                 l2 = l2.next
#                 l3.next = ListNode()
#                 l3 = l3.next
#             if(l1 != None and l2 == None):
#                 old_carry = carry
#                 carry = (l1.val + l3.val + old_carry) // 10
#                 l3.val = (l1.val + l3.val + carry) % 10
#                 l1 = l1.next
#                 l3.next = ListNode()
#                 l3 = l3.next
#             if(l1 == None and l2 != None):
#                 old_carry = carry
#                 carry = (l2.val + l3.val + old_carry) // 10
#                 l3.val = (l2.val + l3.val + carry) % 10
#                 l2 = l2.next
#                 l3.next = ListNode()
#                 l3 = l3.next
                
#             if(carry > 0):
#                 l3.val = (l3.val + carry) % 10
#                 carry = 0
                
            
#             if(l1 == None and l2 == None):
#                 break
        
#         return head_l3