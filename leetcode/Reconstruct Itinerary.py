import collections

class Solution:
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]


class City(object):
    def __init__(self):
        self.to_city = []

a = Solution()
test = [['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']]
test1 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(a.findItinerary(test))
# print(a.findItinerary(test1))