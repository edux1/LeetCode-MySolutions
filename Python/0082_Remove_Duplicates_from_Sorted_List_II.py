# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        ant, act = dummy, dummy.next
        while act and act.next:
            if act.val == act.next.val:
                temp = act.val
                act = act.next
                while act and act.val == temp:
                    act = act.next
                ant.next = act
                
            elif act.val != act.next.val:
                act = act.next
                ant = ant.next

        return dummy.next