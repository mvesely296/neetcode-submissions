class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        new = None

        while head:
            new = ListNode()
            new.next = p
            new.val = head.val
            head = head.next
            p = new

        return new