# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        n2 = []

        # O(n)
        while l1:
            n1.append(l1.val)
            l1 = l1.next

        # O(m)    
        while l2:
            n2.append(l2.val)
            l2 = l2.next

        print(n1)
        #Convert into number
        mul = 1
        m1 = 0

        for i in range(len(n1)):
            m1 += n1[i]*mul
            mul *= 10

        mul = 1
        m2 = 0
        
        for i in range(len(n2)):
            m2 += n2[i]*mul
            mul *= 10
        
        fnum = str(m1 + m2)
        fnum = fnum[::-1]

        res = ListNode(int(fnum[0]))
        curr = res
        for i in range(1,len(fnum)):
            curr.next = ListNode(int(fnum[i]))
            curr = curr.next
        
        return res

        



