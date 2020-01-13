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
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.E):
            node = list(self.E)[self.n]
            visited = {}
            result = []
            for key, value in self.E.items():
                visited[key] = False
            queue = [node]
            visited[node] = True
            while queue:
                s = queue.pop(0)
                result.append(s)
                for i in self.E[node]:
                    if visited[i] is False:
                        queue.append(i)
                        visited[i] = True
                self.n += 1
                return s

        else:
            raise StopIteration


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertix in graph:
    print(vertix)
