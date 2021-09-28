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


    for name,nick in reader:

         vertex = User(name,nick)

         insta.add(vertex)


"""
Esse bloco inidca o nodo de origem, nodo de destino e o peso desta conexão
"""

with open('conexoes.csv') as csvfile:

    reader = csv.reader(csvfile)


    for source,dst,weight in reader:
        
        pass

print(insta.adjacency)        	
        