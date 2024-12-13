from bridge_comp import Graph
from kruskal import Kruskal


class FiberNet:
    def __init__(self) -> None:
        self.n = 0
        self.m = 0
        self.edges = []

        self.read_and_validate_input()


        kruskal = Kruskal(self.n, self.edges)
        self.mst, self.total_cost = kruskal.kruskal_mst()


        graph = Graph(self.n)
        for u, v, weight in self.edges:
            graph.add_edge(u, v)

        self.analysis_result = graph.analyze_graph()

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
                if not (1<=w<=1000000):
                    raise ValueError

        except ValueError:
            print("BŁĄD")
            exit()

    def __str__(self) -> str:
        output = []

        output.append("MINIMALNE DRZEWO SPINAJĄCE:")
        for edge in self.mst:
            output.append(f"{edge[0]} {edge[1]} {edge[2]}")
        output.append(f"Łączny koszt: {self.total_cost}")

        output.append("")

        output.append("MOSTY:")
        if self.analysis_result["bridges"]:
            for u, v in sorted(self.analysis_result["bridges"]):
                output.append(f"{u} {v}")
        else:
            output.append("BRAK MOSTÓW")

        output.append("")

        output.append("KOMPONENTY:")
        components = self.analysis_result["components"]
        formatted_components = " ".join(f"[{' '.join(map(str, component))}]" for component in components)
        output.append(f"{len(components)} KOMPONENTY: {formatted_components}")

        return "\n".join(output)
    
if __name__ == "__main__":
    FiberNet()