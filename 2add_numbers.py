# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        carry = 0
        while(True):
            print(l3.val)
            if(l1 != None and l2 != None):
                carry = (l1.val + l2.val) // 10
                l3.val += (l1.val + l2.val) % 10                    
                l1 = l1.next
                l2 = l2.next
                new_node = ListNode()
                l3.next = new_node
                l3 = l3.next
            if(l1 != None and l2 == None):
                old_carry = carry
                carry = (l1.val + old_carry) // 10
                l3.val += (l1.val + carry) % 10
                l1 = l1.next
                new_node = ListNode()
                l3.next = new_node
                l3 = l3.next
            if(l1 == None and l2 != None):
                old_carry = carry
                carry = (l2.val + old_carry) // 10
                l2 = l2.next
                new_node = ListNode()
                l3.next = new_node
                l3 = l3.next
                
            if(carry > 0):
                l3.val += carry
                carry = 0
            
            if(l1 == None and l2 == None):
                break
        
        return l3
                
        
        