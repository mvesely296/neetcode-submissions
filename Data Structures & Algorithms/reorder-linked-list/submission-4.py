class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        right = slow.next
        slow.next = None

        right_reversed, curr = None, right
        while curr:
            tmp = curr.next
            curr.next = right_reversed
            right_reversed = curr
            curr = tmp

        curr = head
        while right_reversed:
            tmp1, tmp2 = right_reversed.next, curr.next
            curr.next = right_reversed
            right_reversed.next = tmp2
            right_reversed, curr = tmp1, tmp2

        return