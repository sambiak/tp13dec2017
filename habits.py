from random import shuffle
g = dict()
CHAUSSURE = "chaussure"
CHAUSSETTE = "chaussette"
MONTRE = "montre"
PANTALON = "pantalon"
CEINTURE = "ceinture"
CHEMISE = "chemise"
PULL = "pull"
MANTEAU = "manteau"
CEINTURE = "ceinture"

g[CHAUSSETTE]  = [None, ["chaussure"]]
g[MONTRE] = [None, []]
g[CHAUSSURE] = [None, []]
g[CEINTURE] = [None, []]
g[MANTEAU] = [None, []]
g["pantalon"] = [None, ["ceinture", CHAUSSURE]]
g[CHEMISE] = [None,[CEINTURE, PULL]]
g[PULL] = [None,[MANTEAU]]
g["r"] = [None, [CHAUSSURE, CHAUSSETTE, MONTRE, PANTALON, CEINTURE, CHEMISE, PULL, MANTEAU, CEINTURE]]

def DFS(x, graph, value):
    for voisin in graph[x][1]:

        if not graph[voisin][0]:
            value = DFS(voisin, graph, value)
    graph[x][0] = value + 1
    return value + 1





def DFS2(x, graph, value):
    pile = [x]
    while pile:
        x = pile.pop()
        print(x)
        if not graph[x][0]:
            for voisin in graph[x][1]:
                if not graph[voisin][0]:
                    pile.append(x)
                    pile.append(voisin)
                    break
            else:
                graph[x][0] = value + 1
                value = value + 1


DFS2("r", g, 1)
l = []
for key in g.keys():
    l.append((g[key][0], key))
trie = sorted(l, key= lambda tup: tup[0], reverse=True)
print(l)
print(trie)
print(g)