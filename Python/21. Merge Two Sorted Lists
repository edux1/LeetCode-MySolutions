# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
            head = list2
            cur = list2
            list2 = list2.next
        else:
            head = list1
            cur = list1
            list1 = list1.next

        while list1 != None and list2 != None:
            if list1.val > list2.val:
                cur.next = list2
                cur = list2
                list2 = list2.next
            else:
                cur.next = list1
                cur = list1
                list1 = list1.next

        if list1 == None:
            cur.next = list2
        elif list2 == None:
            cur.next = list1
        return head