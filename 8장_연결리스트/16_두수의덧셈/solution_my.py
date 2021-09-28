# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()

        while l1:
            s = ListNode(l1.val + l2.val)
            print(s)
            l1 = l1.next
            l2 = l2.next

        return s