from enum import Enum

class ReadVersion(Enum):
    STEPIK = "stepik"
    MANUAL = "manual"



class Graphs:
    def __init__(self) -> None:
        self.AdjacencyListAsDict = {}
        self.Matrix = []
        self.InOutDegList = []
        self.Exercise7Queries = []
        self.Exercise7Answers = []

    def GetAdjacencyListAsDict(self) -> dict[int, list[int]]:
        return self.AdjacencyListAsDict
    
    def GetMatrix(self) -> list[list[int]]:
        return self.Matrix
    
    def GetInOutDegList(self) -> list[list[int, int]]:
        return self.InOutDegList
    
    def GetExercise7Queries(self) -> list:
        return self.Exercise7Queries

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

    def ReadAdjacencyMatrix(self, version: ReadVersion) -> None:
        if version == ReadVersion.STEPIK:
            while True:
                try:
                    a = input()
                    self.Matrix.append(list(map(int,a.split())))
                except EOFError:
                    break

        if version == ReadVersion.MANUAL:
            while True:
                a = input()
                if not a:
                    break
                self.Matrix.append(list(map(int,a.split())))

    def Exercise7ReadInput(self) -> list:
        """reads adjacency list, reads and appends all the queries to queries list"""
        self.AdjacencyListAsDict = eval(input())
        q = int(input())
        for _ in range(q):
            self.Exercise7Queries.append(input())

    def ConvertMatrixIntoAList(self) -> None:
        if not self.Matrix:
            print("empty matrix")
            return

        self.AdjacencyListAsDict.clear()

        for i, row in enumerate(self.Matrix):
            node = i+1
            adjacent_nodes = [j+1 for j, connection in enumerate(row) if connection > 0]
            self.AdjacencyListAsDict.update({node:adjacent_nodes})

    def ConvertListIntoAMatrix(self) -> None:
        if not self.AdjacencyListAsDict:
            print("empty dict")
            return
        
        self.Matrix.clear()
        amount_of_nodes = len(self.AdjacencyListAsDict)
        for key in list(self.AdjacencyListAsDict.keys()):
            row = []
            for j in range(amount_of_nodes):
                if j+1 in self.AdjacencyListAsDict[key]:
                    row.append(1)
                else:
                    row.append(0)
            self.Matrix.append(row)

    def CountInAndOutDeg(self) -> None:
        """counts in and out degrees, only works with adjacency list"""
        if not self.AdjacencyListAsDict:
            print("empty dict")
            return
        
        self.InOutDegList.clear()

        for _ in range(len(self.AdjacencyListAsDict)):
            self.InOutDegList.append([0, 0])
        
        for key, values in self.AdjacencyListAsDict.items():
            self.InOutDegList[key-1][1] = len(values)
            for value in values:
                self.InOutDegList[value-1][0] += 1

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
    
    def Exercise7TransformQueries(self) -> None:
        transformed_queries = []
        for query in self.Exercise7Queries:
            querySplit = query.split()
            queryTransformed = [x if x.isalpha() else int(x) for x in querySplit]
            transformed_queries.append(queryTransformed)
        self.Exercise7Queries = transformed_queries

    def Exercise7AnswerQueries(self) -> None:
        for query in self.Exercise7Queries:
            if query[0] == "neighbours":
                amounOfNeighbours = self.GetAmountOfNeighbours(query[1])
                self.Exercise7Answers.append(amounOfNeighbours)
            elif query[0] == "connection":
                areNodesConnected = self.AreNodesConnected(query[1], query[2])
                self.Exercise7Answers.append(areNodesConnected)

    def Exercise7PrintAnswers(self) -> None:
        for answer in self.Exercise7Answers:
            if answer is True:
                print('Yes')
            elif answer is False:
                print('No')
            else:
                print(answer)

        
    def PrintInAndOutDegList(self) -> None:
        """prints out the list like stepik needs it to"""
        print("Stopnie wejściowe: ", end='')

        for i in range(len(self.InOutDegList)):
            if i != len(self.InOutDegList) - 1:
                print(self.InOutDegList[i][0], end=' ')
            else:
                print(self.InOutDegList[i][0])

        print("Stopnie wyjściowe: ", end='')

        for i in range(len(self.InOutDegList)):
            if i != len(self.InOutDegList) - 1:
                print(self.InOutDegList[i][1], end=' ')
            else:
                print(self.InOutDegList[i][1])

    def PrintDictAsAdjacencyList(self) -> None:
        for key, value in self.AdjacencyListAsDict.items():
            print(key, value)

    def PrintAdjacencyMatrix(self) -> None:        
        for row in self.Matrix:
            print(' '.join(map(str,row)))



grafy = Graphs()
#grafy.ReadAdjacencyMatrix(ReadVersion.MANUAL)
#grafy.ReadAdjacencyList(ReadVersion.MANUAL)
#grafy.PrintAdjacencyMatrix()
#grafy.ConvertMatrixIntoAList()
#grafy.PrintDictAsAdjacencyList()
#print(grafy.GetAmountOfNeighbours(2))
#print(grafy.AreNodesConnected(7, 2))
grafy.Exercise7ReadInput()
grafy.Exercise7TransformQueries()
grafy.Exercise7AnswerQueries()
grafy.Exercise7PrintAnswers()