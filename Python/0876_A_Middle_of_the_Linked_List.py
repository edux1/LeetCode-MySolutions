# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        count = 0
        while head.next:
            head = head.next
            if count%2 == 0:
                p = p.next
            count += 1
        return p
