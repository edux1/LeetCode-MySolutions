# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1, p2 = head, head
        count = 0
        while p1.next:
            count += 1
            p1 = p1.next
        count -= n
        while count > 0:
            p2 = p2.next
            count -= 1
        if not p2.next:
            return None
        if count == -1:
            return head.next
        p2.next = p2.next.next
        return head