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

    users = []
    for name,nick in reader:


         insta.createAccount(User(name,nick))

         users.append(vertex)

users = {user.username: user for user in users}

"""
Esse bloco inidca o nodo de origem, nodo de destino e o peso desta conexão
"""

with open('conexoes.csv') as csvfile:

    reader = csv.reader(csvfile)


    for src,dst,pref in reader:


         insta.follow(str(src),str(dst),pref)




    for source,dst,weight in reader:
        follower = users[source] 
        followed = users[dst]
        insta.follow(follower, followed, int(weight))

username = "helena42"
user = users[username]
anotherUsername = "isadora45"
anotherUser = users[anotherUsername]

print(f'\nquantidade de seguidores de {username} {insta.followersNumber(user)}') 
print(f'\nquantidade de amizades de {username} é {insta.followingNumber(user)}') 
print(f'\nos stories de {username} : {insta.getStories(user)}') 
print(f'\nOs top influencer são\n')
insta.topInfluencers(6)
print(f'\nO caminho de {username} para {anotherUsername} é\n')
insta.followingPath(user, anotherUser) 

