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


        if l < n and self.compare_nodes(self.heap[l], self.heap[largest]):
            largest = l


        if r < n and self.compare_nodes(self.heap[r], self.heap[largest]):
            largest = r


        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]


            self.heapify(n, largest)

    def compare_nodes(self, node1, node2):
        if node1[2] != node2[2]:
            return node1[2] > node2[2]
        if node1[0] != node2[0]:
            return node1[0] > node2[0]
        return node1[1] > node2[1]

    def heap_sort(self):
        n = len(self.heap)

        #build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)


        for i in range(n-1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]  
            self.heapify(i, 0)


if __name__ == "__main__":
    data = [
    (1, 2, 3),
    (2, 3, 3),
    (3, 4, 3),
    (4, 5, 3),
    (5, 6, 3),
    (6, 1, 3),
    (1, 4, 3),
    (2, 5, 3)
]

    heap = MaxHeapSort(data)
    print(heap.heap)
