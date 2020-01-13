"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        self.visited = {node: False for node in list(self.E.keys())}
        self.node = list(self.E.keys())[0]
        self.queue = [self.node]
        return self

    def __next__(self):
        while self.queue:
            s = self.queue.pop(0)
            self.visited[s] = True
            for i in self.E[s]:
                if i not in self.queue:
                    if self.visited[i] is False:
                        self.queue.append(i)
            return s

        else:
            raise StopIteration


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
G = {'D': ['A'], 'B': ['C'], 'A': ['B', 'C', 'D'], 'C': []}
graph = Graph(E)
graphG = Graph(G)

for vertix in graphG:
    print(vertix)
