class CriticalPoints: 
    def __init__(self, n, edges):
        self.n = n
        self.graph = {i: [] for i in range(1, n+1)}
        self.time = 0

        for x, y, z in edges:
            self.add_edge(x, y)

        self.critical_points = self.find_critical_points()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, u, parent, visited, disc, low, critical_points):
        visited[u] = True
        self.time += 1
        disc[u] = self.time
        low[u] = self.time

        children = 0

        #v being neighbour
        for v in self.graph[u]: 
            if not visited[v]:
                children += 1
                #recursivly we check for neighbours dfs, u parent, visited obvious, disc - discovery time of eahc node (time=steps), low - lowest dicorvery time from each node,critical points obv
                #print(f"PREDFS\nNode: {u}\nNeighbor: {v}\nVisted: {visited}\nDiscovery: {disc}\nLow:{low}\nCritical points: {critical_points}\n")
                self.dfs(v, u, visited, disc, low, critical_points)
                #print(f"POSTDFS\nNode: {u}\nNeighbor: {v}\nVisted: {visited}\nDiscovery: {disc}\nLow:{low}\nCritical points: {critical_points}")

                #basically check for no cycles ?
                #print(f"low[{u}], low[{v}]\n")
                low[u] = min(low[u], low[v])

                #if u is not a root and there is no edge that would connect it some other way mean that if we remove the vertex its oging to disconnect the graph
                if parent is not None and low[v] >= disc[u]:
                    critical_points.add(u)

            elif v != parent:
                #print(f"ELIF\nNode: {u}\nNeighbor: {v}\nVisted: {visited}\nDiscovery: {disc}\nLow:{low}\nCritical points: {critical_points}\n")
                #print(f"low[{u}], disc[{v}]")
                low[u] = min(low[u], disc[v])

        #root exception
        if parent is None and children > 1:
            critical_points.add(u)
        #print(f"POSTDFS\nNode: {u}\nNeighbor: {v}\nVisted: {visited}\nDiscovery: {disc}\nLow:{low}\nCritical points: {critical_points}")

    def find_critical_points(self):
        visited = {i: False for i in range(1, self.n + 1)}
        disc = {i: float('inf') for i in range(1, self.n + 1)}
        low = {i: float('inf') for i in range(1, self.n + 1)}
        critical_points = set()

        
        self.dfs(1, None, visited, disc, low, critical_points)

        #checks if graph is connected bcs all the visited vales should be true
        #print(visited,disc,low)
        for value in visited.values():
            if value != True:
                #error
                return None

        return critical_points



if __name__ == "__main__":
    n = 5
    edges = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (3, 5, 4), (4, 5, 5)]
    cp = CriticalPoints(n, edges)
    print(f"Punkty krytyczne w grafie to: {cp.critical_points}")
