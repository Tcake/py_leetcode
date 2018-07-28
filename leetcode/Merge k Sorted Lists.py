# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import bisect


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        head = ListNode(0)
        p = head
        list_len = len(lists)
        now_val_list = [lists[i].val if lists[i] else None for i in range(list_len)]
        sort_list = sorted([now_val_list[i] for i in range(list_len) if now_val_list[i] is not None])
        while True:
            if len(sort_list) == 0:
                break
            now_count = sort_list.pop(0)

            now_index = now_val_list.index(now_count)
            lists[now_index] = lists[now_index].next
            if lists[now_index]:
                bisect.insort_left(sort_list, lists[now_index].val)
                now_val_list[now_index] = lists[now_index].val
            else:
                now_val_list[now_index] = None

            p.next = ListNode(now_count)
            p = p.next
        return head.next


a = Solution()
test = ListNode(0)
t = test
for i in (0, 2, 5):
    t.next = ListNode(i)
    t = t.next
print(a.mergeKLists([test.next]))

# import functools
#
#
# class Solution:
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#
#         arrayList = list()
#         for linkList in lists:
#             ptr = linkList
#             while ptr:
#                 arrayList.append(ptr.val)
#                 ptr = ptr.next
#
#         ret = ListNode('header')
#         arrayList.sort()
#
#         def f(x, y):
#             x.next = ListNode(y)
#             return x.next
#
#         functools.reduce(f, arrayList, ret)
#         ret = ret.next
#
#         return ret