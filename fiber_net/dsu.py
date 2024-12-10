class DisjointSetUnion:
    def __init__(self, n):
        # Initialize parent and rank arrays
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find roots of the sets to which x and y belong
        root_x = self.find(x)
        root_y = self.find(y)

        # If they are already in the same set, do nothing
        if root_x == root_y:
            # print(f"Union skipped for {x}-{y}, already connected.")
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # If ranks are the same, promote one root and increment its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        # print(f"Union successful for {x}-{y}")
        return True

# # Example usage:
# n = 5  # Number of elements
# dsu = DisjointSetUnion(n)

# # Initially, each element is its own parent
# print("Initial parent array:", dsu.parent)

# # Union some sets
# dsu.union(0, 1)
# dsu.union(1, 2)
# dsu.union(3, 4)

# print("Parent array after unions:", dsu.parent)

# # Find representatives
# print("Representative of 0:", dsu.find(0))
# print("Representative of 3:", dsu.find(3))
# print("Parent array after find operations (path compression):", dsu.parent)
