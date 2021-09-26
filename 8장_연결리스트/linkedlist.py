class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#node에 데이터 추가
a1 = ListNode("a1")
a2 = ListNode("a2")
a3 = ListNode("a3")
a4 = ListNode("a4")

#각 노드를 연결
a1.next = a2
a2.next = a3
a3.next = a4

print(a1.val)
print(a1.next.val)

head = a1
while head is not None:
    print(head.val)
    head = head.next