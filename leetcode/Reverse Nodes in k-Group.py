# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(node_s, times):
            left = node_s
            right = node_s.next
            while times > 1:
                tmp = right.next
                right.next = left
                left = right
                right = tmp
                times -= 1
            return left

        if k == 1:
            return head

        start = head
        end = start
        front = head
        result = None
        flag = True
        while True:
            for _ in range(k):
                if end is not None:
                    end = end.next
                else:
                    flag = False
                    break
            if not flag:
                break
            res = reverse(start, k)
            if not result:
                result = res
            else:
                front.next = res
                front = start

            start = end
        if result:
            front.next = start
        else:
            result = head

        return result


a = Solution()
test = ListNode(1)
h_test = test
for i in range(10):
    test.next = ListNode(i+2)
    test = test.next

show_list = []
result = a.reverseKGroup(h_test, 2)
# result = h_test
while result:
    print(result.val)
    result = result.next

# class Solution:
#     def reverseKGroup(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#         nh = head
#         nt = None
#         p = head
#         while p is not None:
#             s = p
#             for i in range(0, k):
#                 if p is None:
#                     return nh
#                 p = p.next
#             rv = self.reverse(s, p)
#             if nt is not None:
#                 nt.next = rv
#             else:
#                 nh = rv
#             nt = s
#             s.next = p
#         return nh
#
#
#     def reverse (self, begin, end):
#         h = None
#         while begin != end:
#             tmp = begin.next
#             begin.next =h
#             h = begin
#             begin = tmp
#         return h

