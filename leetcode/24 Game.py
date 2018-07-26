import math
import itertools


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return math.isclose(nums[0], 24)
        return any(self.judgePoint24([x] + rest)
                   for a, b, *rest in itertools.permutations(nums)
                   for x in {a + b, a - b, a * b, b and a / b})


# class Solution:
#     def judgePoint24(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         def add(x,y):
#             return x+y
#         def minus(x,y):
#             return x-y
#         def _minus(x,y):
#             return y-x
#         def mul(x,y):
#             return x * y
#         def div(x,y):
#             return x/y
#         def _div(x,y):
#             return y/x
#         calculate = [add,minus,_minus,mul,div,_div]
#
#         def canGet24(card):
#
#             try:
#                 if len(card) == 2:
#                     # return card[0]+card[1] == 24 or card[0]-card[1]==24 or card[1]-card[0]==24 or card[0] * card[1]==24 or card[0]/card[1]==24 or card[1]/card[0]==24
#                     for fun in calculate:
#                         if(abs(24 - fun(card[0],card[1])) < 0.000000000001):
#                             return True
#                     return False
#
#                 if len(card) == 3:
#                     for fun in calculate:
#                         x,y,z = card
#                         if canGet24([x,fun(y,z)]) == True:
#                             return True
#                         if canGet24([y,fun(x,z)]) == True:
#                             return True
#                         if canGet24([z,fun(x,y)]) == True:
#                             return True
#                     return False
#                 for fun in calculate:
#                     a,b,c,d = card
#                     if canGet24([fun(a,b),c,d]) == True:
#                         return True
#                     if canGet24([fun(a,c),b,d]) == True:
#                         return True
#                     if canGet24([fun(a,d),b,c]) == True:
#                         return True
#                     if canGet24([fun(b,c),a,d]) == True:
#                         return True
#                     if canGet24([fun(b,d),a,c]) == True:
#                         return True
#                     if canGet24([fun(c,d),a,b]) == True:
#                         return True
#                 return False
#             except ZeroDivisionError:
#                 return False
#         return canGet24(nums)
