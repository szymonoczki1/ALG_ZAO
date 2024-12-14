class ArticulationPoints: 
    def __init__(self, n, edges):
        self.n = n
        self.graph = {i: [] for i in range(1, n+1)}

        for x, y, z in edges:
            self.add_edge(x, y)

        self.articulation_points = self.find_articulation_points()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_articulation_points(self):
        visited = {i: False for i in self.graph}
        parent = {i: None for i in self.graph}
        low = {i: float('inf') for i in self.graph}
        discovery = {i: float('inf') for i in self.graph}
        time = 0
        articulationpoints = []

        def dfs(node):
            nonlocal time
            visited[node] = True
            time += 1
            discovery[node] = low[node] = time
            children = 0

            for neighbor in sorted(self.graph[node]):
                if not visited[neighbor]:
                    children += 1
                    parent[neighbor] = node
                    dfs(neighbor)
                    
                    low[node] = min(low[node], low[neighbor])

                    if parent[node] is not None and low[neighbor] >= discovery[node]:
                        articulationpoints.append(node)

                elif neighbor != parent[node]:
                    low[node] = min(low[node], discovery[neighbor])

            if parent[node] is None and children > 1:
                articulationpoints.append(node)

        dfs(1)

        for value in visited.values():
            if value != True:
                #error graph not connected
                return None

        return sorted(articulationpoints)

    


if __name__ == "__main__":
    n = 5
    edges = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (3, 5, 4), (4, 5, 5)]
    #edges = [(1, 2, 4), (2, 3, 3), (3, 4, 5), (4, 5, 2), (5, 6, 5), (6, 1, 4), (2, 4, 6), (3, 5, 4)]
    #edges = [(1, 2, 5)]
    #edges = [(1, 2, 5), (2, 3, 5), (3, 4, 5), (4, 5, 5), (5, 6, 5), (1, 6, 5), (2, 5, 5)]
    ap = ArticulationPoints(n, edges)
    print(f"?{ap.articulation_points}")
    #print(f"Punkty krytyczne w grafie to: {cp.critical_points}")
