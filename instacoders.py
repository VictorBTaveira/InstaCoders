from graph import Graph
import math

class InstaCoders(Graph):

    def __init__(self) -> None:
        super().__init__()
        self.users = {} # creates a mapping of users to classes acess  # each member by the refernece 
       

    def createAccount(self, user):
        super().add(user)
        self.users[user.username] = user

    def deleteAccount(self, user):
        super().delete(user)
        del self.users[user]

    def follow(self, follower, followed, bestFriend):
        super().addArrow(follower, followed, bestFriend)

    def unfollow(self, follower, followed):
        super().removeArrow(follower, followed)

    def followingNumber(self, user):
        return super().outDegree(user)

    def followersNumber(self, user):
        return super().inDegree(user)

    def topInfluencers(self, k):
        inDegrees = [(v, self.inDegree(v)) for v in self.adjacency.keys()]
        inDegrees = self.quicksort(inDegrees, sortBy="followers")
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
            end = len(inDegrees) - 1
            tops = dict(inDegrees[end:end - k:-1])
        finally:
            return tops

    def printTopInfluencers(self, k):
        topInfluencers = self.topInfluencers(k)
        if topInfluencers:
            print("{:4} {:20} {:>9}".format("Rank", "User", "Followers"))
            for i, user in enumerate(topInfluencers.keys()):
                followersNumber = topInfluencers[user]
                print("{:^4} {:<20} {:^9}".format(i+1, user.username, followersNumber))

    def getStories(self, user):
        stories = list()
        for i in range(2, 0, -1):
            friendshipGroup = [x for x in self.adjacency[user].keys() if self.adjacency[user].get(x) == i]
            friendshipGroup = self.quicksort(friendshipGroup)
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

    def quicksort(self, _list, begin=0, end=None, sortBy=None):
        if end is None:
            end = len(_list) - 1

        if (end - begin) > 0:
            index = self.partition(_list, begin, end, sortBy)
            self.quicksort(_list, begin, index-1, sortBy)
            self.quicksort(_list, index+1, end, sortBy)
        return _list

    def partition(self, _list, begin, end, sortBy=None):
        sep = begin
        pivot = _list[end]
        for i in range(begin, end):
            if sortBy: # followers
                elementValue = _list[i][1]
                pivotValue = pivot[1]
            else:
                elementValue = _list[i].username
                pivotValue = pivot.username

            if elementValue < pivotValue:
                _list[i], _list[sep] = _list[sep], _list[i]
                sep += 1
        _list[sep], _list[end] = _list[end], _list[sep]
        return sep