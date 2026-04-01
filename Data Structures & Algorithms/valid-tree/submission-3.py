class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True
        graph = {}

        for ele in edges:
            [i, j] = ele

            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)
            if j not in graph:
                graph[j] = [i]
            else:
                graph[j].append(i)

        visited = set()
        def dfs(k, prev, visited):
            if k in visited:
                return False
            visited.add(k)
            for neighbor in graph.get(k, []):
                if neighbor != prev:
                    if not dfs(neighbor, k, visited):
                        return False
            return True
        
        return dfs(0, -1, visited) and len(visited) == n