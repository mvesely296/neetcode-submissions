class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode()
        head = ListNode(0, current)

        while list1 or list2:
            if (not list1) or (list2 and list2.val < list1.val):
                new = ListNode(list2.val)
                current.next = new
                current = current.next
                list2 = list2.next
            else:
                new = ListNode(list1.val)
                current.next = new
                current = current.next
                list1 = list1.next

        head = head.next.next

        return head