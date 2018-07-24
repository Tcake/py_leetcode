# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        pointer = head
        add_val = 0
        p = l1
        q = l2
        while p is not None or q is not None :
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = add_val + x + y
            add_val = sum / 10
            pointer.next = ListNode(sum % 10)
            pointer = pointer.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if add_val > 0:
            pointer.next = ListNode(1)
        return head.next
