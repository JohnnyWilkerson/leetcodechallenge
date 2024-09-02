# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        onebeforestart = ListNode(0,head)

        one = onebeforestart
        two = onebeforestart

        for i in range(n + 1):
            one = one.next
        while one != None:
            two = two.next
            one = one.next
        
        nodetoremove = two.next

        two.next = nodetoremove.next

        return onebeforestart.next