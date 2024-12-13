class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = {i: [] for i in range(1, n+1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited, component: list, graph):
        visited[node] = True
        component.append(node)

        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                self.dfs(neighbor, visited, component, graph)

    def find_components(self, graph):
        visited = {i: False for i in self.graph}
        components = []

        for node in graph:
            if not visited[node]:
                component = []
                self.dfs(node, visited, component, graph)
                components.append(sorted(component))

        return components

    def find_bridges(self):
        visited = {i: False for i in self.graph}
        parent = {i: None for i in self.graph}
        time = 0
        low = {i: float('inf') for i in self.graph}
        discovery = {i: float('inf') for i in self.graph}
        bridges = []

        def dfs(node):
            nonlocal time
            visited[node] = True
            time += 1
            discovery[node] = low[node] = time

            for neighbor in sorted(self.graph[node]):
                #nie sprawdzamy visited bo to juz beda backedge w dfsie
                #print(f"Neighbor: {neighbor}\nNode: {node}\nlow[node]: {low[node]}\nlow[neighbor]: {low[neighbor]}\n")
                #print(f"tablica low: {low}\ntablica discovery: {discovery}")
                if not visited[neighbor]:
                    parent[neighbor] = node
                    dfs(neighbor)
                    #po wejsciu do ostatniego wierzcholka uzywajac dfs mamy przypisanych rodzicow wszystkich wierzcholkow oprocz korzenia
                    #po rekurencji sprawdzamy od ostatniego wierzcholka w dfs ilosc czasu do przejscia do jego sasiadow ktorych nie b, przypisujemy min od rodzica i samego wierzcholka
                    
                    low[node] = min(low[node], low[neighbor])
                    #print(f"tablica lowPOPRZYISANIU: {low}\ntablica discovery: {discovery}")

                    #if discovery[node] is less or equal to low[neighbor] then the connection is not a brdige
                    #whatever A-B discovery time of A needs to be smaller than lowest possible discovery time of B for the connection to be a brdige
                    if low[neighbor] > discovery[node]:
                        #print(f"DODANY MOST {bridges}")
                        bridges.append((min(node, neighbor), max(node, neighbor)))

                elif neighbor != parent[node]:
                    #print(f"{neighbor} != {parent[node]}\n rodzic {node}\n{low[node]} = min({low[node]},{discovery[neighbor]})")
                    low[node] = min(low[node], discovery[neighbor])

        #print(self.graph.items())
        for node in self.graph:
            if not visited[node]:
                dfs(node)

        #after for loop it looks like this for graph

        # 0:[1,2]
        # 1:[0,2]
        # 2:[0,1,3]
        # 3:[2,4]
        # 4:[3]


        #Node	Visited	Parent	Discovery	Low	Bridges
        #0	    True	None	1	        1	
        #1	    True	0	    2	        1	
        #2	    True	1	    3	        1	(2, 3)
        #3	    True	2	    4	        4	(3, 4)
        #4	    True	3	    5	        5	

        #https://www.thealgorists.com/Algo/GraphTheory/Tarjan/Bridges


        return bridges

    def analyze_graph(self):
        bridges = self.find_bridges()

        graph_copy = {k: v.copy() for k, v in self.graph.items()}
        for u, v in bridges:
            graph_copy[u].remove(v)
            graph_copy[v].remove(u)

        components = self.find_components(graph_copy)

        return {
            "components": components,
            "bridges": bridges
        }





if __name__ == "__main__":
    n, m = 4, 4
    edges = [
        (1,2,1),
        (1,3,1),
        (2,3,1),
        (2,4,1)
    ]


    graph = Graph(n)

    for u, v, cost in edges:
        graph.add_edge(u, v)

    analysis_result = graph.analyze_graph()


    print("MOSTY:")
    if analysis_result["bridges"]:
        for u, v in sorted(analysis_result["bridges"]):
            print(f"{u} {v}")
    else:
        print("BRAK MOSTÓW")

    print("\nKOMPONENTY:")
    components = analysis_result["components"]
    print(len(components), "KOMPONENTY:", " ".join(map(str, components)))