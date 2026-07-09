class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while True:
            if (not slow) or (not fast) or (not slow.next) or (not fast.next) or (not fast.next.next):
                return False
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True