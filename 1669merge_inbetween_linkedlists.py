# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        nodeBeforeCutoff = None
        nodeAfterCutoff = None
        startList1 = list1
        startList2 = list2
        if list1 != None and list2 != None:
            while list1 != None:
                if count+1 == a:
                    nodeBeforeCutoff = list1
                    # print(count, nodeBeforeCutoff.val)

                if count == b:
                    nodeAfterCutoff = list1.next
                    # print(count, nodeAfterCutoff.val)
                count += 1
                list1 = list1.next

            while list2 != None:
                if list2.next == None:
                    list2.next = nodeAfterCutoff
                    break
                list2 = list2.next
            list2 = startList2
            print(startList2)

            list1 = startList1
            while list1.val != nodeBeforeCutoff.val:
                list1 = list1.next

            list1.next = startList2


