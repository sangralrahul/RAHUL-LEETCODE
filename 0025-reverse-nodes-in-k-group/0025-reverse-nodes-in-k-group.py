from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        while True:
            node = group_prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next
            group_next = node.next
            prev = group_next
            curr = group_prev.next
            while curr is not group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            tail = group_prev.next
            group_prev.next = prev
            group_prev = tail