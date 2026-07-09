class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr = head = ListNode()
        carry_over = 0

        while l1 or l2 or carry_over:
            curr.next = ListNode()
            curr = curr.next

            first = l1.val if l1 else 0
            second = l2.val if l2 else 0

            current_val = first + second + carry_over
            if current_val >= 10:
                current_val -= 10
                carry_over = 1
            else:
                carry_over = 0

            curr.val = current_val

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
