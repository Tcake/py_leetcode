class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        if [] in graph:
            return 0

        l_graph = len(graph)
        all_nodes = []
        for i in range(l_graph):
            all_nodes.append(i)

        result = []

        def slave(now_node, path, no_nodes):
            if not no_nodes:
                result.append(len(path))
            if len(now_node) == 1:
                slave(graph[path[-1]], path + now_node, no_nodes)
            else:
                for next in now_node:
                    if next == path[-1]:
                        continue


