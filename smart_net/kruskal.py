from dsu import DisjointSetUnion
from maxheapsort import MaxHeapSort

class Kruskal:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

    def kruskal_mst(self):
        mst = []
        total_cost = 0
        dsu = DisjointSetUnion(self.n)

        #sort edges
        heap = MaxHeapSort(self.edges)
        #get sorted list of edges from heap
        sorted_edges = heap.heap

        for edge in sorted_edges:
            u, v, weight = edge
            if dsu.union(u-1, v-1):
                total_cost += weight
                mst.append(edge)

            # Stop when we have exactly V-1 edges in MST
            if len(mst) == self.n - 1:
                break

        return mst, total_cost


if __name__ == "__main__":
    n = 6

    # List of edges: (vertex1, vertex2, weight)
    data = [
    (1, 2, 4),
    (2, 3, 3),
    (3, 4, 5),
    (4, 5, 2),
    (5, 6, 5),
    (6, 1, 4),
    (2, 4, 6),
    (3, 5, 4)
]
    kruskal = Kruskal(n, data)
    mst, total_cost = kruskal.kruskal_mst()

    print("Edges in the Minimum Spanning Tree (MST):")
    for u, v, weight in mst:
        print(f"({u}, {v}) with weight {weight}")

    print(f"Total cost of the MST was {total_cost}")