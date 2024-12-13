from minheapv2 import minHeap

class Dijkstra:
    def __init__(self, n, edges=[]):
        self.n = n
        self.graph = {i: [] for i in range(1, n + 1)}

        for x, y, z in edges:
            self.add_edge(x, y, z)

        self.distance_matrix = self.compute_distance_matrix()
        self.diameter = self.graph_diameter(self.distance_matrix)
        self.radius = self.graph_radius(self.distance_matrix)
        self.center = self.graph_center(self.distance_matrix)
        self.periphery = self.graph_periphery(self.distance_matrix)

    def add_edge(self, x, y, z):
        if 1 <= x <= self.n and 1 <= y <= self.n:
            self.graph[x].append((y, z))
            self.graph[y].append((x, z))

    def calculate_shortest_paths_from_node(self, start):
        inf = float('inf')
        #row of distances to other nodes from start node / init full of infinities
        distances = [inf] * (self.n + 1)
        distances[start] = 0
        heap = minHeap([(0, start)])

        while heap.heap:
            current_distance, current_vertex = heap.heap[0]

            heap.heap_remove()

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heap.heap_insert((distance, neighbor))

        return distances

    def compute_distance_matrix(self):
        matrix = [[float('inf')] * self.n for _ in range(self.n)]

        for node in range(1, self.n + 1):
            dist = self.calculate_shortest_paths_from_node(node)
            for target in range(1, self.n + 1):
                matrix[node - 1][target - 1] = dist[target]


        return matrix
    
    def graph_diameter(self, matrix):
        return max([max(row) for row in matrix if float('inf') not in row])

    def graph_radius(self, matrix):
        return min([max(row) for row in matrix if float('inf') not in row])

    def graph_center(self, matrix):
        radius = self.graph_radius(matrix)
        return [i+1 for i in range(len(matrix)) if max(matrix[i]) == radius]

    def graph_periphery(self, matrix):
        diameter = self.graph_diameter(matrix)
        return [i+1 for i in range(len(matrix)) if max(matrix[i]) == diameter]


if __name__ == "__main__":
    n = 4
    m = 4
    edges = [(1, 2, 1), (2, 3, 1), (3, 4, 2), (1,3,4)]
    graph = Dijkstra(n, edges)

    print(graph.diameter)
    print(graph.radius)
    print(graph.center)
    print(graph.periphery)

    for row in graph.distance_matrix:
        print(" ".join(map(str, row)))