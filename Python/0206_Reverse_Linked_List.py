# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        last = head
        head = head.next  
        last.next = None
        while head:
            cur = head
            head = head.next
            cur.next = last
            last = cur
        return last