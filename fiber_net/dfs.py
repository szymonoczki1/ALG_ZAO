from stos import Stack



class DFS:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.adjacency_list_as_dict = {}
        self.visited_vertices = []
        self.discovery = {}
        self.low = {}
        self.parent = {}
        self.time = 0
        self.bridges = []
        self.components = []

        self.stack = Stack()
        self.build_adjacency_list()
        self.starting_vertex = list(self.adjacency_list_as_dict.keys())[0]

        self.find_bridges()
        self.find_components()

        print(self)

    def build_adjacency_list(self):
        for u, v, w in self.edges:
            if u not in self.adjacency_list_as_dict:
                self.adjacency_list_as_dict[u] = []
            if v not in self.adjacency_list_as_dict:
                self.adjacency_list_as_dict[v] = []
            self.adjacency_list_as_dict[u].append(v)
            self.adjacency_list_as_dict[v].append(u)

    def find_bridges(self):
        for vertex in self.adjacency_list_as_dict:
            self.discovery[vertex] = -1
            self.low[vertex] = -1
            self.parent[vertex] = None

        self.dfs_bridge(self.starting_vertex)

        self.bridges.sort()

    def find_components(self):
        for bridge in self.bridges:
            self.adjacency_list_as_dict[bridge[0]].remove(bridge[1])
            self.adjacency_list_as_dict[bridge[1]].remove(bridge[0])
        
        visited = set()
        components = []

        def dfs_components(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in self.adjacency_list_as_dict[node]:
                if neighbor not in visited:
                    dfs_components(neighbor, component)

        for node in self.adjacency_list_as_dict:
            if node not in visited:
                component = []
                dfs_components(node, component)
                components.append(component)

        self.components = components

    

    def dfs_bridge(self, u):
        self.visited_vertices.append(u)
        self.discovery[u] = self.low[u] = self.time
        self.time += 1

        for v in self.adjacency_list_as_dict[u]:
            if self.discovery[v] == -1:  # v is not visited
                self.parent[v] = u
                self.dfs_bridge(v)

                # Update low value of u for child v
                self.low[u] = min(self.low[u], self.low[v])

                # Check if the edge (u, v) is a bridge
                if self.low[v] > self.discovery[u]:
                    self.bridges.append((u, v))
            elif v != self.parent[u]:  # Back edge case
                self.low[u] = min(self.low[u], self.discovery[v])

    def get_bridges_components(self):
        return self.bridges, self.components

    def __str__(self):
        return f"Connected Components: {self.components}\nBridges: {self.bridges}"




# Sample input edges
edges = [
    (1, 2, 1),
    (2, 3, 2),
    (4, 5, 3),
    (5, 6, 4),
    (6, 4, 5)   
]

dfs = DFS(edges)
