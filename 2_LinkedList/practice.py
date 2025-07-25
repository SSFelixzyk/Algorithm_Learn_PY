class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast = head
        slow = head

        if fast.next is None:
            return

        while fast:
            if fast == slow:
                index2 = fast
                break
            fast = fast.next.next
            slow = slow.next
        
        if fast is None:
            return
        
        index1 = head

        while index1 != index2:
            index1 = index1.next
            index2 = index2.next
        
        return index1

s = Solution()
head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(0)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next  # Creating a cycle for testing
result = s.detectCycle(head)

