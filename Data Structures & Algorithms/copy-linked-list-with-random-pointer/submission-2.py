import copy
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        dict_initial = {}
            
        p = head 
        first = Node(p.val)


        dict_initial[p] = first

        while p.next:
            p = p.next
            el = Node(p.val)
            dict_initial[p] = el
        
        s = head
        t = first
        while s:
            if s.next:
                t.next = dict_initial[s.next]
            if s.random:
                t.random = dict_initial[s.random]
            s = s.next
            t = t.next
        return first