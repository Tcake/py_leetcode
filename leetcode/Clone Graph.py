from collections import defaultdict
from copy import deepcopy

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        new_node = deepcopy(node)
        self.cache = {}
        self.slave(node, new_node)

        return new_node

    def slave(self, old, new):
        if old.label in self.cache:
            return
        self.cache[old.label] = True
        for i, nd in enumerate(old.neighbors):
            new.neighbors[i] = deepcopy(nd)

        for i, nd in enumerate(old.neighbors):
            self.slave(nd, new.neighbors[i])
