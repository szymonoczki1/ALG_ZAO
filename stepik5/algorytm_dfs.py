from stos import Stack
from readVersionEnum import ReadVersion


class DFS():
    def __init__(self) -> None:
        self.stack = Stack()
        self.adjacency_list_as_dict = {}
        self.visited_vertices = []
        self.starting_vertex = None
        self.is_graph_connected = None


        self.read_adjacency_list_as_dict(ReadVersion.MANUAL)

        self.runDFS()
        self.check_is_graph_connected()

        print(self)

    def read_adjacency_list_as_dict(self, version):
        if version == ReadVersion.STEPIK:
            while True:
                try:
                    a = input()
                    a = a.split()
                    node = int(a[0])
                    #zczytywanie wiercholka startowego
                    if node in self.adjacency_list_as_dict:
                        self.starting_vertex = node
                    else:
                        #sort bo pan mowil ze moze je mieszac
                        adjacent_nodes = sorted(list(map(int,a[1:])))
                        self.adjacency_list_as_dict.update({node:adjacent_nodes})       
                except EOFError:
                    break

        if version == ReadVersion.MANUAL:
            while True:
                a = input()
                if not a:
                    break
                a = a.split()
                node = int(a[0])
                if node in self.adjacency_list_as_dict:
                    self.starting_vertex = node
                else:
                    adjacent_nodes = sorted(list(map(int,a[1:])))
                    self.adjacency_list_as_dict.update({node:adjacent_nodes})

    def get_unvisited_neighbours(self, key: int) -> list[int]:
        unvisited_neighbours = []
        for neighbour in self.adjacency_list_as_dict[key]:
            if neighbour not in self.visited_vertices:
                unvisited_neighbours.append(neighbour)
        return unvisited_neighbours

    def check_is_graph_connected(self):
        if len(self.adjacency_list_as_dict) == len(self.visited_vertices):
            self.is_graph_connected = True
        else:
            self.is_graph_connected = False

    def runDFS(self):
        self.visited_vertices.append(self.starting_vertex)
        self.stack.push(self.starting_vertex)
        while not self.stack.is_empty():
            if self.get_unvisited_neighbours(self.stack.peek()):
                smallest_univisited_neighbour = min(self.get_unvisited_neighbours(self.stack.peek()))

                self.stack.push(smallest_univisited_neighbour)
                self.visited_vertices.append(smallest_univisited_neighbour)
            else:
                self.stack.pop()
                
        
        


    def __str__(self) -> str:
        output = []
        if self.is_graph_connected == True:
            output.append(f"Porządek DFS: {" ".join(map(str, self.visited_vertices))}")
            output.append("Graf jest spójny")
        else:
            output.append("Graf jest niespójny")
        
        return "\n".join(output)

    
DFS()