from graph import Graph
from sort import sort

class InstaCoders(Graph):

    def __init__(self) -> None:
        super().__init__()

    def followingNumber(self, user):
        super().outDegree(user.username)

    def followersNumber(self, user):
        super().inDegree(user.username)

    def topInfluencers(self, k):
        topInfluencers = super().topIncomingVertices(k)
        if topInfluencers:
            print("{:3} {:15} {:9}".format("Rank", "Username", "Followers"))
            for i, username in enumerate(topInfluencers.keys()):
                print("{:3} {:15} {:9}".format(i, username, topInfluencers[username]))

    def followingPath(self, source, target):
        super().printPath(source, target)

    def getStories(self, user):
        stories = tuple()
        for i in range(2, 0, -1):
            friendshipGroup = [x for x in self.adjacency.keys() if self.adjacency.get(x) == i]
            sort(friendshipGroup)
            stories += friendshipGroup
        
        return stories
