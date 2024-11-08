from enum import Enum

class ReadVersion(Enum):
    STEPIK = 1
    MANUAL = 2



class Graphs:
    def __init__(self) -> None:
        self.AdjacencyListAsDict = {}
        self.DegreeSequence = []
        self.AmountOfNodes = 0
        self.AmountOfEdges = 0
        self.AverageDegree = 0

        self.ReadAdjacencyList(ReadVersion.MANUAL)

        self.CalculateAmountOfNodes()
        self.CalculateDegreeSequence()
        self.CalculateAmountOfEdges()
        self.CalculateAverageDegree()

        self.isACompleteGraph = self.CheckIfGraphIsComplete()
        self.isACycle = self.CheckIfGraphIsACycle()
        self.isAPath = self.CheckIfGraphIsAPath()
        self.isATree = self.CheckIfGraphIsATree()
        self.isAHypercube = self.CheckIfGraphIsAHypercube()
        
        print(self)

    def ReadAdjacencyList(self, version: ReadVersion) -> None:
        if version == ReadVersion.STEPIK:
            while True:
                try:
                    a = input()
                    a = a.split()
                    node = int(a[0])
                    adjacent_nodes = list(map(int,a[1:]))
                    self.AdjacencyListAsDict.update({node:adjacent_nodes})       
                except EOFError:
                    break

        if version == ReadVersion.MANUAL:
            while True:
                a = input()
                if not a:
                    break
                a = a.split()
                node = int(a[0])
                adjacent_nodes = list(map(int,a[1:]))
                self.AdjacencyListAsDict.update({node:adjacent_nodes})


    def GetAmountOfNeighbours(self, key: int) -> int:
        """returns number of neighbours of given node, only works with adjacency list"""
        if key in self.AdjacencyListAsDict:
            return len(self.AdjacencyListAsDict[key])
        else:
            raise ValueError(f"{key} not in dictionary")
        
    def AreNodesConnected(self, node1: int, node2: int) -> bool:
        """checks if nodes are connected, returns true or false, only works with adjacency list"""
        for node in (node1, node2):
            if node not in self.AdjacencyListAsDict:
                raise ValueError(f"{node} doesnt exist")
        
        return node2 in self.AdjacencyListAsDict[node1]
    
    def CalculateAmountOfNodes(self) -> None:
        self.AmountOfNodes = len(self.AdjacencyListAsDict)
    
    def CalculateAmountOfEdges(self) -> None:
        """Calculates amount of edges based on the formula degSum//2, degSum being the sum of every degree in the graph"""
        degSum = 0
        for deg in self.DegreeSequence:
            degSum += deg
        self.AmountOfEdges = degSum // 2

    def CalculateDegreeSequence(self) -> None:
        self.DegreeSequence = []
        for values in self.AdjacencyListAsDict.values():
            self.DegreeSequence.append(len(values))

    def CalculateAverageDegree(self) -> None:
        for deg in self.DegreeSequence:
            self.AverageDegree += deg
        self.AverageDegree = self.AverageDegree / len(self.DegreeSequence)

    def CheckIfGraphIsComplete(self) -> bool:
        """Checks if the number of edges is equal to (n*(n-1))/2, n being the number of nodes"""
        n = len(self.AdjacencyListAsDict)
        expectedAmountOfEdges = (n*(n-1))/2
        return self.AmountOfEdges == expectedAmountOfEdges
    
    def CheckIfGraphIsACycle(self) -> bool:
        """Checks if every degree is equal to 2"""
        for deg in self.DegreeSequence:
            if deg != 2:
                return False
        return True
    
    def CheckIfGraphIsAPath(self) -> bool:
        """Checks if exactly 2 degrees are equal to 1 and all the other ones are equal to 2"""
        degOne = 0
        for deg in self.DegreeSequence:
            if deg == 1:
                degOne += 1
            elif deg != 2:
                return False
        return degOne == 2
    
    def CheckIfGraphIsATree(self) -> bool:
        """Checks if there is no isolated nodes and if the amount of edges equals to n-1, n being the number of nodes"""
        noIsolatedNodes = True
        for deg in self.DegreeSequence:
            if deg == 0:
                noIsolatedNodes = False
        return self.AmountOfEdges == self.AmountOfNodes - 1 and noIsolatedNodes == True
    
    def CheckIfGraphIsAHypercube(self) -> bool:
        """Checks if every degree is the same and if the amount of nodes is equal to 2^d, d being a degree"""
        d = self.DegreeSequence[0]
        return len(set(self.DegreeSequence)) == 1 and pow(2,d) == self.AmountOfNodes

    def __str__(self) -> str:
        output = []
        output.append(f'Ilość wierzchołków: {self.AmountOfNodes}')
        output.append(f'Ilość krawędzi: {self.AmountOfEdges}')
        output.append(f'Stopnie wierzchołków: {" ".join(map(str, self.DegreeSequence))}')
        output.append(f'Średni stopień: {self.AverageDegree:.2f}')

        graph_types = [(self.isACompleteGraph, "Jest to graf pełny"), (self.isACycle, "Jest to cykl"), (self.isAPath, "Jest to ścieżka"), (self.isATree, "Jest to drzewo"), (self.isAHypercube, "Jest to hiperkostka")]

        
        counter = 0
        for graph_type in graph_types:
            if graph_type[0] == True:
                output.append(graph_type[1])
                counter += 1

        if counter == 0:
            output.append("Graf nie należy do żadnej z podstawowych klas.")

        return '\n'.join(output)




Graphs()