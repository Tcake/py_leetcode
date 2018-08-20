class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        l_ring = len(ring)
        ring_cache = {}
        for i, s in enumerate(ring):
            if s in ring_cache:
                ring_cache[s].append(i)
            else:
                ring_cache[s] = [i,]

        ring_index = 0
        result = 0
        for item in key:
            tmp = 101
            for index in ring_cache[item]:
                q, p = (ring_index, index) if ring_index < index else (index, ring_index)
                m = min(p - q, l_ring - p + q)
                if m < tmp:
                    tmp = m
                    min_index = index
                    print(tmp, index, q, p, item)
            ring_index = min_index
            result += tmp + 1

        return result


a = Solution()
ring = "godding"
key = "gd"
ring1 = "abcde"
key1 = "ade"
ring2 = "caotmcaataijjxi"
key2 = "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
print(a.findRotateSteps(ring2, key2))
