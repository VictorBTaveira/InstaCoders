import math
class Graph():
    def __init__(self) -> None:
        self.adjacency = {}

    def add(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}

    def delete(self, vertex):
        if vertex in self.adjacency:
            del self.adjacency[vertex]

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

    def djikstra(self, origin):
        return self._djikstra(origin, self.adjacency)
                
    def _djikstra(self, origin, adjacency=None):
        if adjacency is None:
            adjacency = self.adjacency
        distance = {vertex: math.inf for vertex in adjacency.keys()}
        distance[origin] = 0
        
        previous = {vertex: None for vertex in adjacency.keys()}
        
        visited = []
        notVisited = distance.copy()
        
        while len(notVisited) > 0:
            currentVertex = sorted(notVisited.items(), key=lambda x: x[1])[0][0]
            del notVisited[currentVertex]
            visited.append(currentVertex)
            
            for adjacent in adjacency[currentVertex]:
                if adjacent not in visited:
                    newDistance = distance[currentVertex] + adjacency[currentVertex][adjacent]
                    if newDistance < distance[adjacent]:
                        distance[adjacent] = newDistance
                        notVisited[adjacent] = newDistance
                        previous[adjacent] = currentVertex
    
        return distance, previous

    def _pathDJK(self, origin, destination):
        previous = {}
        if origin in self.adjacency.keys() and destination in self.adjacency.keys():
            distances, previous = self.djikstra(origin)
            if distances[destination] == math.inf:
                previous.clear()
        return previous

    def _path(self, origin, destination, search=None):
        if search == "BFS":
            return self._pathBFS(origin, destination)
        return self._pathDJK(origin, destination)

    def straightPath(self, origin, destination, search=None):
        visited = self._path(origin, destination, search)
        path = list()
        
        if visited:
            path.append(destination)
            previous = visited[destination]
            while previous:
                path.append(previous)
                previous = visited[previous]
            path.reverse()
            
        return path

    def printPath(self, origin, destination, search=None) -> None:
        path = self.straightPath(origin, destination, search)
        if path:
            output = " -> ".join(path)
        else:
            output = f"There is no path between {origin} and {destination}."
        print(output)
