from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None         


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:  # O(1)
            return False               # O(1)
        slow = fast = head             # O(1)
        while fast and fast.next:      # O(n)
            slow = slow.next           # O(1)
            fast = fast.next.next      # O(1)
            if slow == fast:           # O(1)
                return True            # O(1)
        return False                   # O(1)


if __name__ == '__main__':
    s = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = head
    print(s.hasCycle(head))
