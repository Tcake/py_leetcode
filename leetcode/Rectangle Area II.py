# import NumArray

class Solution:
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]] + [0]))
        # st = NumArray(xs)
        # L = []
        # for x1, y1, x2, y2 in rectangles:
        #     L.append([y1, 1, x1, x2])
        #     L.append([y2, -1, x1, x2])
        # L.sort()
        # cur_y = cur_x_sum = area = 0
        # for y, sig, x1, x2 in L:
        #     area += (y - cur_y) * cur_x_sum
        #     cur_y = y
        #     cur_x_sum = st.update(x1, x2, sig)
        # return area % (10 ** 9 + 7)

        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]] + [0]))
        x_i = {v: i for i, v in enumerate(xs)}
        count = [0] * len(x_i)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        # print(L)
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
            # print(xs,xs[1:],count)
        return area % (10 ** 9 + 7)


a = Solution()
test = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
test1 = [[0,0,1000000000,1000000000]]
print(a.rectangleArea(test))
