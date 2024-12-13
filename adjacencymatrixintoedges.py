def matrix_to_edges(matrix):
    edges = []
    for i, row in enumerate(matrix):
        for j in range(i,len(row)):
            if row[j] != 0:
                edges.append((i+1,j+1,row[j]))

    return edges

# def matrix_to_edges(matrix):
#     edges = []
#     num_nodes = len(matrix)
#     for i in range(num_nodes):
#         for j in range(i + 1, num_nodes):  # Only consider the upper triangular part
#             if matrix[i][j] != 0:
#                 edges.append((i+1, j+1, matrix[i][j]))

#     return edges


matrix = [[0, 0, 0, 10],
          [0, 0, 5, 5],
          [0, 5, 0, 7],
          [10, 5, 7, 0]]

print(matrix_to_edges(matrix))
