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
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow