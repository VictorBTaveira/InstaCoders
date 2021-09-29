from graph import Graph
from mysort import mySort
import math

class InstaCoders(Graph):

    def __init__(self) -> None:
        super().__init__()

    def createAccount(self, user):
        super().add(user)

    def follow(self, follower, followed, bestFriend):
        super().addArrow(follower, followed, bestFriend)

    def unfollow(self, follower, followed):
        super().removeArrow(follower, followed)

    def followingNumber(self, user):
        return super().outDegree(user)

    def followersNumber(self, user):
        return super().inDegree(user)

    def topInfluencers(self, k):
        topInfluencers = super().topIncomingVertices(k)
        if topInfluencers:
            print("{:4} {:20} {:>9}".format("Rank", "User", "Followers"))
            for i, user in enumerate(topInfluencers.keys()):
                followersNumber = topInfluencers[user]
                print("{:^4} {:<20} {:^9}".format(i+1, user.username, followersNumber))

    def getStories(self, user):
        stories = list()
        for i in range(2, 0, -1):
            friendshipGroup = [x for x in self.adjacency[user].keys() if self.adjacency[user].get(x) == i]
            friendshipGroup = mySort(friendshipGroup)
            stories += friendshipGroup
        
        return stories

    def djikstra(self, origin):
        adjacency = self.adjacency.copy()
        for vertex in adjacency.keys():
            for adjacent in adjacency[vertex].keys():
                adjacency[vertex][adjacent] = adjacency[vertex][adjacent]%2 + 1
        return super()._djikstra(origin, adjacency)

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
            output = " -> ".join(user.username for user in path)
        else:
            output = f"There is no path between {origin} and {destination}."
        print(output)

    def followingPath(self, origin, destination):
        self._printPath(origin, destination)
