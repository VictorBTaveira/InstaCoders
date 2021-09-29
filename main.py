import csv 

from instaCodersUser import User

from instacoders import InstaCoders

insta = InstaCoders()

"""
    esse cria os nodos da instacoders,
    lê cada linha e separa o nome em name 
    e o username em nick
"""
with open('usuarios.csv') as csvfile:

    reader = csv.reader(csvfile)

    for name, username in reader:

         user = User(name, username)

         insta.createAccount(user)


"""
Esse bloco inidca o nodo de origem, nodo de destino e o peso desta conexão
"""
with open('conexoes.csv') as csvfile:

    reader = csv.reader(csvfile)

    for source, dst, weight in reader:
        follower = insta.users[source] 
        followed = insta.users[dst]
        insta.follow(follower, followed, int(weight))

username = "helena42"
user = insta.users[username]
anotherUsername = "isadora45"
anotherUser = insta.users[anotherUsername]

print(f'\nquantidade de seguidores de {username} {insta.followersNumber(user)}') 
print(f'\nquantidade de amizades de {username} é {insta.followingNumber(user)}') 
print(f'\nos stories de {username} : {insta.getStories(user)}') 
print(f'\nOs top influencer são\n')
insta.printTopInfluencers(6)
print(f'\nO caminho de {username} para {anotherUsername} é\n')
insta.followingPath(user, anotherUser) 