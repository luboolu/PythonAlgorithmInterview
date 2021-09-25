from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        q1: List = []
        q2: List = []

        node1 = l1
        node2 = l2
        # 리스트 변환
        while node1 is not None:
            q1.append(node1.val)
            node1 = node1.next

        while node2 is not None:
            q2.append(node2.val)
            node2 = node2.next

        merge = sorted(q1 + q1)
        merge_list = []
        for m in merge:
            merge_list.append(ListNode(m))

        for i, m in enumerate(merge_list):
            if i < len(merge) - 1:
                merge_list[i].next = merge_list[i + 1]

        return merge_list

sol = Solution()
print(sol.mergeTwoLists([1,2,4],[1,3,4]))