class Graph:
    def __init__(self, v):
        self.V = v
        self.edges = []

    def addEdge(self, u, v, w):
        self.edges.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def kruskal(self):
        self.edges.sort(key=lambda x: x[2])
        parent = []
        for i in range(self.V):
            parent.append(i)
        print("Edge\tWeight")
        count = 0
        i = 0
        while count < self.V - 1:
            u, v, w = self.edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                print(u, "-", v, "\t", w)
                self.union(parent, x, y)
                count += 1

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.kruskal()