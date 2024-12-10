from stack import Stack
from stable_quicksort import QuickSort

class DFS():
    def __init__(self, matrix: list[list[int]], starting_vertex: int, exit_vertices: list[int] = [], check_connectivity = False) -> None:
        self.matrix = matrix
        self.visited_vertices = []
        self.stack = Stack()
        self.starting_vertex = starting_vertex
        self.exit_vertices = exit_vertices
        self.check_connectivity = check_connectivity

    def run_dfs(self):
        self.stack.push(self.starting_vertex)
        self.visited_vertices.append(self.starting_vertex)

        while self.stack.is_empty() == False:
            checked_vertex = self.stack.peek()
            
            if self.check_connectivity == False:
                if checked_vertex in self.exit_vertices:
                    return True, self.visited_vertices
            
            #collection of neighbouring vertices
            neighbours = []
            #check vertex -1 bcs if matrix is nxn n being 6, indexes are from 0 to 5 and our vertices are from 1 to 6
            for neighbour_index in range(len(self.matrix[checked_vertex-1])):
                #+1 in neighbour_index to properly represent a vertex
                if self.matrix[checked_vertex-1][neighbour_index] == 1 and neighbour_index + 1 not in self.visited_vertices:
                    neighbours.append(neighbour_index+1)

            #sorting with stable quicksort in ascending order
            if neighbours:
                neighbours = QuickSort(neighbours).sort()
                self.stack.push(neighbours[0])
                self.visited_vertices.append(neighbours[0])
            else:
                self.stack.pop()
        
        #when stack is empty and check_connectivity true
        if self.check_connectivity == True:
            return len(self.visited_vertices) == len(self.matrix), self.visited_vertices

        #when stack is empty
        return False, None

# matrix = [
#     [0, 0, 1, 1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 0],
#     [1, 0, 0, 0, 1, 0, 1, 1],
#     [1, 0, 0, 0, 1, 0, 1, 1],
#     [0, 1, 1, 1, 0, 0, 1, 0],
#     [1, 1, 0, 0, 0, 0, 1, 0],
#     [0, 0, 1, 1, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0, 0, 0]
# ]

# # matrix = [
# #     [0, 0],
# #     [0, 0]
# # ]

# matrix = [
#     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
# ]

# print(DFS(matrix, 3, [8],check_connectivity=True).run_dfs()[1])