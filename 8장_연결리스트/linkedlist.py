class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#node에 데이터 추
a1 = ListNode("a1")
a2 = ListNode("a2")

#각 노드를 연결
a1.next = a2

print(a1.val)
print(a1.next.val)



