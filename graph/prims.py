class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = [[0] * v for _ in range(v)]

    def prim(self):
        selected = [False] * self.V
        selected[0] = True
        print("Edge\tWeight")
        for _ in range(self.V - 1):
            minimum = 999
            x = 0
            y = 0
            for i in range(self.V):
                if selected[i]:
                    for j in range(self.V):
                        if not selected[j] and self.graph[i][j]:
                            if self.graph[i][j] < minimum:
                                minimum = self.graph[i][j]
                                x = i
                                y = j
            print(x, "-", y, "\t", self.graph[x][y])
            selected[y] = True

g = Graph(5)
g.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
g.prim()