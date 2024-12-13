from dsu import DisjointSetUnion
from maxheapsort import MaxHeapSort

class Kruskal:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def kruskal_mst(self):
        mst = []
        total_cost = 0
        dsu = DisjointSetUnion(self.vertices)


        heap = MaxHeapSort(self.edges)
        sorted_edges = heap.heap

        for edge in sorted_edges:
            u, v, weight = edge
            if dsu.union(u-1, v-1):
                total_cost += weight
                mst.append(edge)

            if len(mst) == self.vertices - 1:
                break

        return mst, total_cost


if __name__ == "__main__":
    vertices = 6

    data = [
    (1, 2, 1),
    (2, 3, 2),
    (4, 5, 3),
    (5, 6, 4),
    (6, 4, 5)
]
    kruskal = Kruskal(vertices, data)
    mst, total_cost = kruskal.kruskal_mst()

    print("Edges in the Minimum Spanning Tree (MST):")
    for u, v, weight in mst:
        print(f"({u}, {v}) with weight {weight}")

    print(f"Total cost of the MST was {total_cost}")