from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        D = defaultdict(list)

        for u, v in edges:
            D[u].append(v)
            D[v].append(u)
        
        seen = set()
        seen.add(source)
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for vertex in D[node]:
                if vertex not in seen:
                    seen.add(vertex)
                    queue.append(vertex)
                    
        return False
