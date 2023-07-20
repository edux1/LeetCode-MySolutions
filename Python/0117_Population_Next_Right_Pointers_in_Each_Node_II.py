"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            ant = root
            if root.left:
                act = root.left
                lvl = root.left
            else:
                act = root.right
                lvl = root.right
            
            while act:
                if ant and ant.left and ant.left != act:
                    act.next = ant.left
                    act = act.next
                elif ant and ant.right and ant.right != act:
                    act.next = ant.right
                    act = act.next
                    ant = ant.next
                elif ant and ant.next:
                    ant = ant.next
                else:
                    ant = lvl
                    if lvl.left:
                        act = lvl.left
                    else:
                        act = lvl.right
                    lvl = act
                if lvl and not lvl.left and not lvl.right and (act and act.left or act.right):
                    lvl = act
        return root