class MaxHeapSort:
    def __init__(self, heap) -> None:
        self.heap = heap
        self.heap_sort()

    def heapify(self, n, i):
        #root
        largest = i
        #left child
        l = 2 * i + 1
        #right child     
        r = 2 * i + 2

        # l<n if its still in our array, compare nodes returns true if left child is supposed to be swapped with parent
        if l < n and self.compare_nodes(self.heap[l], self.heap[largest]):
            largest = l

        # Check if right child exists and is greater than root
        if r < n and self.compare_nodes(self.heap[r], self.heap[largest]):
            largest = r

        # Change root if needed
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]  # Swap

            # Heapify the root
            self.heapify(n, largest)

    def compare_nodes(self, node1, node2):
        # Compare by weight (z) first
        if node1[2] != node2[2]:
            return node1[2] > node2[2]
        # If weights are equal, compare first vertex numbers (x)
        if node1[0] != node2[0]:
            return node1[0] > node2[0]
        # If first vertex numbers are also equal, compare second vertex numbers (y)
        return node1[1] > node2[1]

    def heap_sort(self):
        n = len(self.heap)

        # Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        # Extract elements from the heap
        for i in range(n-1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]  # Swap the root with the last element
            self.heapify(i, 0)

# Sample data
# data = [(1,2,3), (2,1,3), (3,2,1), (5,2,8), (2,2,3)]

# heap = MaxHeapSort(data)
# print(heap.heap)
