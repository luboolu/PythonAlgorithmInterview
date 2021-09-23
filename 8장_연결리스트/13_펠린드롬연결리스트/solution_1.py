from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 펠린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

sol = Solution()
print(sol.isPalindrome([1, 2, 2, 1]))