class MaxHeapSort:
    def __init__(self, heap) -> None:
        self.heap = heap
        self.heap_sort()

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1  
        r = 2 * i + 2

        #check if left child is bigger than its parent
        if l < n and self.compare_nodes(self.heap[l], self.heap[largest]):
            largest = l
        #check if right child is bigger than its parent
        if r < n and self.compare_nodes(self.heap[r], self.heap[largest]):
            largest = r

        #if parent wasnt the max element from himself and his children than swap and heapify again from the child that was swapped as a root/parent all the way to the end of an array
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]  # Swap
            self.heapify(n, largest)

    def compare_nodes(self, node1, node2):
        #weight
        if node1[2] != node2[2]:
            return node1[2] > node2[2]
        #first vertex
        if node1[0] != node2[0]:
            return node1[0] > node2[0]
        #second vertex
        return node1[1] > node2[1]
    
    def compare_nodesv2(self, node1, node2):
        if node1[2] != node2[2]:
            return node1[2] > node2[2]
        if node1[0] < node1[1]:
            if node2[0] < node2[1]:
                return node1[0] < node2[0]
            else:
                return node1[0] < node2[1]
        else:
            if node2[0] < node2[1]:
                return node1[1] < node2[0]
            else:
                return node1[1] < node2[1]


    def heap_sort(self):
        n = len(self.heap)

        #build heap, just heapify everything from last non-leaf element to the top
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        #swap last element with first heapify the array len -1, so the last element in an array is already sorted and not to be touched iterate till only 1 is left
        for i in range(n-1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]  # Swap the root with the last element
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
