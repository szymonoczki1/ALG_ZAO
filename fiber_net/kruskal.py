from dsu import DisjointSetUnion
from heap import MaxHeapSort

class Kruskal:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

    def find_mst(self):
        dsu = DisjointSetUnion(self.n)
        heap = MaxHeapSort(self.edges)
        edges_sorted = heap.heap

        mst = []
        total_cost = 0

        for u, v, w in edges_sorted:
            if dsu.union(u - 1, v - 1):
                print(f"Added edge ({u}, {v}) with weight {w}")
                mst.append((u, v, w))
                total_cost += w

                if len(mst) == self.n - 1:
                    break

        if len(mst) == self.n - 1:
            return mst, total_cost
        else:
            print("Edges in MST:", mst)
            return None, None
        
n = 5  # Number of nodes
m = 7  # Number of edges
edges = [
    (1, 2, 2),
    (2, 3, 3),
    (3, 4, 1),
    (4, 5, 4),
    (5, 1, 5),
    (1, 3, 3),
    (2, 4, 2)
]

# kruskal = Kruskal(n, edges)
# mst, cost = kruskal.find_mst()

# if mst is not None:
#     print("Minimum Spanning Tree (Edges):", mst)
#     print("Total cost of MST:", cost)
# else:
#     print("Graph is not connected and cannot form an MST.")