class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        curr = head

        if n == length:
            return head.next

        for i  in range(length - n - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head