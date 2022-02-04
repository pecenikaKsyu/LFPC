import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

#Ex. 1
# Convert RG to FA
vn_brut = input("Defineste elementele Vn (separandu-le prin spatiu)\n")
vn = vn_brut.split(" ")
vn.append(".")
print("VN = {}".format(vn))

nr_rel = int(input ("Care este numarul de relatii?\n"))
matrice_graph = [[0 for x in range(len(vn))] for y in range(len(vn))];

for k in range(nr_rel) :
    i=0
    j=0
    vertex_start, weight, vertex_terminal = input().split(" ")
    for n in range(len(vn)) :
        if (vn[n] == vertex_start ) : i=n
        if (vn[n] == vertex_terminal) : j=n
    matrice_graph[i][j] = weight
    print(matrice_graph)
#Ex. 2
#Check if there could exist such word in FA
cuvant = input ("Introdu cuvantul spre verificare:\n")
check_var = True
lungime_cuvant = len(cuvant)
h=0
valori_finale = [0 for i in range(len(vn))]
j = len(vn)-1
for i in range(j):
    if (matrice_graph[i][j]!='0') :
        valori_finale[h] = matrice_graph[i][j]
        h=h+1

for k in range(h):
    if (cuvant[lungime_cuvant-1] != valori_finale[k]):
        check_var = False
    else: check_var= True; break;

i=0
for k in range(lungime_cuvant):
    ch=cuvant[k]
    j=0
    if (check_var == True):
        if (matrice_graph[i][j]==ch):
            i=j
            j=0
            check_var = True
    else:
        if (j==len(vn)-1):
            check_var = False
        else: j+=1

if (check_var):
    print("Cuvantul corespunde FA")
else:
    print("Cuvantul nu corespunde FA")



#Ex. 3
#Plot the FA graph
G = nx.DiGraph()

G.add_edges_from([('q1\n{}'.format(vn[0]), 'q0\n{}'.format(vn[1])),('q2\n{}'.format(vn[2]),'q4\n{}'.format("X")),('q3\n{}'.format(vn[3]),'q3\n{}'.format(vn[3]))], label="a")
G.add_edges_from([('q0\n{}'.format(vn[1]),'q1\n{}'.format(vn[0])),('q2\n{}'.format(vn[2]),'q0\n{}'.format(vn[1])),('q3\n{}'.format(vn[3]),'q2\n{}'.format(vn[2]))], label="b")
G.add_edges_from([('q0\n{}'.format(vn[1]),'q3\n{}'.format(vn[3]))], label="d")

edge_labels=dict([((u,v,),d['label'])
                 for u,v,d in G.edges(data=True)])

node_labels = {node:node for node in G.nodes()}
edge_colors = ['black']
node_colors = ['#E2CDF1']
pos=nx.spring_layout(G)
nx.draw_networkx_labels(G, pos, labels=node_labels)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos, node_color = node_colors, node_size=1500,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
pylab.show()