# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if not self.intervals:
            self.intervals.append([val, val])
        else:
            left = 0
            right = len(self.intervals)
            flag = 0
            while left < right:
                mid = (left + right) / 2
                if val < self.intervals[mid][0]:
                    right = mid
                elif val >= self.intervals[mid][0]:
                    left = mid
                if flag == 0 and right - left <= 1:
                    flag += 1
                elif flag == 1:
                    break
            if right == 0:
                if val == self.intervals[right][0] - 1:
                    self.intervals[right][0] -= 1
                else:
                    self.intervals = [[val, val], ] + self.intervals
                return
            if self.intervals[left][0] <= val <= self.intervals[left][1]:
                return
            elif val == self.intervals[left][1] + 1:
                if right != len(self.intervals) and self.intervals[left][1] + 2 == self.intervals[right][0]:
                    self.intervals = self.intervals[:left] + [[self.intervals[left][0], self.intervals[right][1]], ] + self.intervals[right + 1:]
                else:
                    self.intervals[left][1] += 1
            elif right != len(self.intervals) and val == self.intervals[right][0] - 1:
                self.intervals[right][0] -= 1
            else:
                self.intervals = self.intervals[:right] + [[val, val], ] + self.intervals[right:]

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals


a = SummaryRanges()
for i in [49,97,53,5]:
    a.addNum(i)
    print(a.getIntervals())


# class SummaryRanges(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.intervals = []
#
#     def addNum(self, val):
#         """
#         :type val: int
#         :rtype: void
#         """
#         low, high = 0, len(self.intervals) - 1
#         while low <= high:
#             mid = (low + high) // 2
#             elem = self.intervals[mid]
#             if elem.start <= val <= elem.end:
#                 return
#             elif elem.start > val:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#
#         # insert the interval
#         pos = min(low, high) + 1
#         self.intervals[pos:pos] = [Interval(val, val)]
#
#         # merge with next interval
#         if pos + 1 < len(self.intervals) and val == self.intervals[pos + 1].start - 1:
#             self.intervals[pos].end = self.intervals[pos + 1].end
#             self.intervals[pos + 1:pos + 2] = []
#
#         # merge with prev interval
#         if pos - 1 >= 0 and val == self.intervals[pos - 1].end + 1:
#             self.intervals[pos - 1].end = self.intervals[pos].end
#             self.intervals[pos:pos + 1] = []
#
#     def getIntervals(self):
#         """
#         :rtype: List[Interval]
#         """
#         return self.intervals
