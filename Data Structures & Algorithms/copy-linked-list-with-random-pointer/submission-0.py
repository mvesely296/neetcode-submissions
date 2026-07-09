class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap: dict[Node, Node] = {}

        curr = head
        while curr:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next

        newCurr = newHead = nodeMap.get(head)
        curr = head

        while curr:
            newCurr.next = nodeMap.get(curr.next)
            newCurr.random = nodeMap.get(curr.random)
            newCurr = newCurr.next
            curr = curr.next

        return newHead