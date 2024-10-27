from enum import Enum

class ReadVersion(Enum):
    STEPIK = 1
    MANUAL = 2



class Graphs:
    def __init__(self) -> None:
        self.AdjacencyListAsDict = {}
        self.Matrix = []
        self.DegreeSequence = []
        self.AmountOfNodes = 0
        self.AmountOfEdges = 0
        self.AverageDegree = 0

    def GetAdjacencyListAsDict(self) -> dict[int, list[int]]:
        return self.AdjacencyListAsDict
    
    def GetMatrix(self) -> list[list[int]]:
        return self.Matrix
    
    def GetInOutDegList(self) -> list[list[int, int]]:
        return self.InOutDegList

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
            raise ValueError("key not in dictionary")
        
    def AreNodesConnected(self, node1: int, node2: int) -> bool:
        """checks if nodes are connected, only works with adjacency list"""
        for node in (node1, node2):
            if node not in self.AdjacencyListAsDict:
                raise ValueError(f"{node} doesnt exist")
        
        return node2 in self.AdjacencyListAsDict[node1]
    
    def CalculateAmountOfNodes(self) -> None:
        self.AmountOfNodes = len(self.AdjacencyListAsDict)
    
    def CalculateAmountOfEdges(self) -> None:
        self.AmountOfEdges = 0
        for key, values in self.AdjacencyListAsDict.items():
            for value in values:
                if key < value:
                    self.AmountOfEdges += 1

    def CalculateDegreeSequence(self) -> None:
        self.DegreeSequence = []
        for values in self.AdjacencyListAsDict.values():
            self.DegreeSequence.append(len(values))

    def CalculateAverageDegree(self) -> None:
        degSum = 0
        for values in self.AdjacencyListAsDict.values():
            degSum += len(values)
        self.AverageDegree = degSum/len(self.AdjacencyListAsDict)

    def CheckIfGraphIsComplete(self) -> bool:
        pass


    def PrintDegreeSequence(self) -> None:
        print("Stopnie wierzchołków:", end='')
        for deg in self.DegreeSequence:
            print(f' {deg}', end='')
        print()

    def PrintAmountOfNodes(self) -> None:
        print(f'Ilość wierzchołków: {self.AmountOfNodes}')

    def PrintAmountOfEdges(self) -> None:
        print(f'Ilość krawędzi: {self.AmountOfEdges}')

    def PringAverageDegree(self) -> None:
        print(f'Średni stopień {self.AverageDegree:.2f}')

    def PrintDictAsAdjacencyList(self) -> None:
        for key, value in self.AdjacencyListAsDict.items():
            print(key, value)



#inicjalizacja
grafy = Graphs()
#wczytaj liste
grafy.ReadAdjacencyList(ReadVersion.MANUAL)
#liczba wierzcholkow
grafy.CalculateAmountOfNodes()
grafy.PrintAmountOfNodes()
#liczba krawedzi
grafy.CalculateAmountOfEdges()
grafy.PrintAmountOfEdges()
#ciag stopni wierzcholkow nie posortowany
grafy.CalculateDegreeSequence()
grafy.PrintDegreeSequence()
#sredni stopien grafu
grafy.CalculateAverageDegree()
grafy.PringAverageDegree()