class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = curr = fast = ListNode(0, head)

        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            curr = curr.next

        curr.next = curr.next.next

        return start.next