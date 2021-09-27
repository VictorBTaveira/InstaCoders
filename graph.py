class Graph():
    def __init__(self) -> None:
        self.adjacency = {}

    def add(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}

    def addArrow(self, source, target, weight=1):
        if source in self.adjacency:
            self.adjacency[source][target] = weight

    def removeArrow(self, source, target):
        if source in self.adjacency:
            del self.adjacency[source][target]

    def _isAdjacent(self, v, u):
        if u in self.adjacency:
            return v in self.adjacency[u].keys()
        return False

    def outDegree(self, vertex):
        if vertex in self.adjacency.keys():
            return len(self.adjacency[vertex].keys())

    def inDegree(self, vertex):
        if vertex in self.adjacency.keys():
            return sum(self._isAdjacent(vertex, u) for u in self.adjacency.keys())

    def topIncomingVertices(self, k):
        inDegrees = [(v, self.inDegree(v)) for v in self.adjacency.keys()]
        inDegrees = sorted(inDegrees, key=lambda x: x[1], reverse=True)
        tops = None
        try:
            k = int(k)
            if not k > 0:
                raise Exception
        except:
            print("Invalid parameter: k must be a positive integer.")
        else:
            if k > len(self.adjacency.keys()):
                k = len(self.adjacency.keys())
            tops = dict(inDegrees[:k])
        finally:
            return tops
    
    def _pathDFS(self, origin, destination):
        previous = {}
        if origin in self.adjacency and destination in self.adjacency:
            previous[origin] = None
            if not self.existsPathDFS(origin, destination, previous=previous):
                previous.clear()
        return previous

    def _existsPathDFS(self, origin, destination, previous):
        if origin in self.adjacency and destination in self.adjacency:
            if len(previous) == 0:
                previous = {origin: None}

            if origin == destination:
                return True
            
            for neighbor in self.adjacency[origin].keys():
                if neighbor not in previous:
                    previous[neighbor] = origin
                    if self.existsPathDFS(neighbor, destination, previous):
                        return True
            return False
        return False

    def _pathBFS(self, origin, destination):
        previous = {}
        if origin in self.adjacency and destination in self.adjacency:
            previous[origin] = None
            if not self.existsPathBFS(origin, destination, previous=previous):
                previous.clear()
        return previous

    def existsPathBFS(self, origin, destination, previous):
        if origin in self.adjacency and destination in self.adjacency:
            previous[origin] = None
            
            _queue = [origin]
            while _queue:
                atual = _queue.pop(0)
                if atual == destination:
                    return True

                for neighbor in self.adjacency[origin].keys():
                    if neighbor not in previous and neighbor not in _queue:
                        previous[neighbor] = atual
                        _queue.append(neighbor)
            return False
        return False

    def _path(self, origin, destination, search="BFS"):
        if search == "DFS":
            return self._pathDFS(origin, destination)
        return self._pathBFS(origin, destination)

    def straightPath(self, origin, destination, search="BFS") -> tuple:
        visited = self._path(origin, destination, search)
        path = list()
        
        if visited:
            path.append(destination)
            previous = visited[destination]
            while previous:
                path.append(previous)
                previous = visited[previous]
            path.reverse()
            
        return tuple(path)

    def printPath(self, origin, destination, search="BFS") -> None:
        path = self.straightPath(origin, destination, search)
        if path:
            output = " -> ".join(str(vertex) for vertex in path if vertex)
        else:
            output = f"There is no path between {origin} and {destination}."
        print(output)
        