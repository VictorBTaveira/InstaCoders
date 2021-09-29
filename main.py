import csv
from instaCodersUser import User
from instacoders import InstaCoders

def createAccounts(instaCoders, csvFile):
    with open(csvFile, mode="r") as file:
        usersCSV = csv.reader(file)
        users = []
        for line in usersCSV:
            username = User(line[0], line[1])
            users.append(username)
            instaCoders.createAccount(username)

        users = {username.username: username for username in users}
    return users

def makeConnections(instaCoders, users, csvFile):
    with open(csvFile, mode="r") as file:
        connections = csv.reader(file)
        
        for line in connections:
            follower = users[line[0]]
            followed = users[line[1]]
            instaCoders.follow(follower, followed, int(line[2]))

def main():
    insta = InstaCoders()
    users = createAccounts(insta, "usuarios.csv")
    makeConnections(insta, users, "conexoes.csv")

    username = "helena42"
    anotherUsername = "isadora45"
    topNumber = 6

    user = users[username]
    anotherUser = users[anotherUsername]

    print("\nFollowers Number.")
    print(f"{user} has {insta.followersNumber(user)} followers.")

    print("\nFollowing Number.")
    print(f"{user} follow {insta.followingNumber(user)} users.")

    print("\nStories Queue.")
    stories = insta.getStories(user)
    print(user, stories, sep=" - ")

    print("\nPath beetwen users.")
    insta.followingPath(user, anotherUser)

    print("\nTop Influencers.")
    insta.topInfluencers(topNumber)

main()