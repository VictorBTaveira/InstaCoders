from graph import Graph
from sort import mySort
import math

class InstaCoders(Graph):

    def __init__(self) -> None:
        super().__init__()

    def followingNumber(self, user):
        return super().outDegree(user.username)

    def followersNumber(self, user):
        return super().inDegree(user.username)

    def topInfluencers(self, k):
        topInfluencers = super().topIncomingVertices(k)
        if topInfluencers:
            print("{:3} {:15} {:9}".format("Rank", "Username", "Followers"))
            for i, username in enumerate(topInfluencers.keys()):
                print("{:3} {:15} {:9}".format(i, username, topInfluencers[username]))

    def getStories(self, user):
        stories = list()
        for i in range(2, 0, -1):
            friendshipGroup = [x for x in self.adjacency.keys() if self.adjacency.get(x) == i]
            mySort(friendshipGroup)
            stories += friendshipGroup
        
        return stories

    def djikstra(self, origin):
        adjacency = self.adjacency.copy()
        for vertex in adjacency.keys():
            for adjacent in adjacency[vertex].keys():
                adjacency[vertex][adjacent] = adjacency[vertex][adjacent]%2 + 1
        return super().djikstra(origin, adjacency)

    def _pathDJK(self, origin, destination):
        previous = {}
        if origin in self.adjacency.keys() and destination in self.adjacency.keys():
            distances, previous = self.djikstra(origin)
            if distances[destination] == math.inf:
                previous.clear()
        return previous

    def straightPath(self, origin, destination, search=None):
        visited = self._pathDJK(origin, destination)
        path = list()
        
        if visited:
            path.append(destination)
            previous = visited[destination]
            while previous:
                path.append(previous)
                previous = visited[previous]
            path.reverse()
            
        return path

    def _printPath(self, origin, destination, search=None) -> None:
        path = self.straightPath(origin, destination, search)
        if path:
            output = " -> ".join(path)
        else:
            output = f"There is no path between {origin} and {destination}."
        print(output)

    def followingPath(self, origin, destination):
        self._printPath(origin, destination)
