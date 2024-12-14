from dijkstry import Dijkstra
from kruskal import Kruskal
from articulation_points import ArticulationPoints

class SmartNet:
    def __init__(self) -> None:
        self.n = 0
        self.m = 0
        self.edges = []

        self.read_and_validate_input()

        self.ap = ArticulationPoints(self.n, self.edges)

        #checks if graph is connected
        if self.ap.articulation_points == None:
            print("BŁĄD")
            exit()

        kruskal = Kruskal(self.n, self.edges)
        self.mst, self.total_cost = kruskal.kruskal_mst()

        

        graph1 = Dijkstra(self.n, self.edges)

    

        self.distance_matrix = graph1.distance_matrix
        self.diameter = graph1.diameter
        self.radius = graph1.radius
        self.center = graph1.center
        self.periphery = graph1.periphery

        print(self)

    def read_and_validate_input(self):
        try:
            first_line = input().split()
            self.n = int(first_line[0])
            self.m = int(first_line[1])

            if not (2<=self.n<=100):
                raise ValueError
            
            if not ((self.n-1)<=self.m<=(self.n*(self.n-1)/2)):
                raise ValueError

            for _ in range(self.m):
                edge = list(map(int, input().split()))
                if edge[0] > edge[1]:
                    edge[0], edge[1] = edge[1], edge[0]
                self.edges.append(tuple(edge))

            for a,b,w in self.edges:
                if not (1<=a<=self.n):
                    raise ValueError
                if not (1<=b<=self.n):
                    raise ValueError
                if not (1<=w<=1000):
                    raise ValueError

        except ValueError:
            print("BŁĄD")
            exit()
        

    def __str__(self) -> str:
        output = []

        output.append("SIEĆ PODSTAWOWA (MST):")
        for edge in self.mst:
            output.append(f"{edge[0]}-{edge[1]}: {edge[2]}")
        output.append(f"Łączny czas: {self.total_cost}")

        output.append("")

        output.append("PARAMETRY SIECI:")
        output.append(f"Średnica: {self.diameter}")
        output.append(f"Promień: {self.radius}")
        output.append(f"Centrum: {self.center}")
        output.append(f"Peryferium: {self.periphery}")

        output.append("")

        output.append("CZASY PRZEJAZDÓW:")
        for row in self.distance_matrix:
            output.append(" ".join(map(str, row)))

        output.append("")

        output.append("PUNKTY KRYTYCZNE:")
        if self.ap.articulation_points:
            output.append(f"{" ".join(map(str,self.ap.articulation_points))}")
        else:
            output.append("BRAK")

        return "\n".join(output)
    
if __name__ == "__main__":
    SmartNet()