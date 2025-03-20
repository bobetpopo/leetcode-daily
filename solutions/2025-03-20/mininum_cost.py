# Problem: 3108. Minimum Cost Walk in Weighted Graph (hard)

# Solution 1: Union-find

# Notes: due to how bitwise AND works for adding up path costs, the lowest cost from vertex a to vertex b is the
#          walk going through as many edges as possible.
#        ANDing a new cost to the current cost creates a new cost that can only be equal to or lower than the 
#          current cost. Also, a AND a = a, so you can go back and forth all edges in a connected component
#          to get the minimum cost, since backtracking doesn't add cost.
#        Thus, the best way to achieve the lowest cost is traversing each edge in a connected component
#        We can use a disjoint set (union-find) data structure to find the components.
#        Then we calculate the total cost in a component by taking the AND of all its edge weights.

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        self.parent = [-1] * n
        self.depth = [0] * n

        # set accumulator to be -1 since in binary -1 = 111...1
        component_cost = [-1] * n

        # use union to build the parent array
        for edge in edges:
            self._union(edge[0], edge[1])

        # for each edge, find the parent of one of its vertices, then AND its cost to the edge cost
        for edge in edges:
            root = self._find(edge[0])
            component_cost[root] &= edge[2]

        answer = []
        for q in query:
            start, end = q
            if self._find(start) != self._find(end):
                answer.append(-1)
            else:
                root = self._find(start)
                answer.append(component_cost[root])
        
        return answer

    def _find(self, node):
        if self.parent[node] == -1:
            return node
        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]
    
    def _union(self, node1, node2):
        root1 = self._find(node1)
        root2 = self._find(node2)
        if root1 == root2:
            return
        # swap root 1 and root 2 if root 1 is smaller; we want to make root 2 child of root 1
        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1

        self.parent[root2] = root1

        # update depth of root 1 if root 1 and root 2 are of same depth
        if self.depth[root1] == self.depth[root2]:
            self.depth[root1] += 1