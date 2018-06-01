import sys
import gensim, logging

import networkx  as nx

import matplotlib.pyplot as plt 

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

m = 'ruscorpora_upos_skipgram_300_5_2018.vec.gz'
if m.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
else:
    model = gensim.models.KeyedVectors.load(m)

model.init_sims(replace=True)

arr = ['дорога_NOUN', 'путь_NOUN', 'улица_NOUN', 'проспект_NOUN', \
       'маршрут_NOUN', 'шоссе_NOUN', 'трасса_NOUN', 'магистраль_NOUN', \
       'путешествие_NOUN', 'переулок_NOUN', 'поездка_NOUN', 'линия_NOUN', \
       'тур_NOUN', 'турне_NOUN', 'экскурсия_NOUN', 'перемещение_NOUN', \
       'площадь_NOUN', 'эстакада_NOUN', 'гонка_NOUN', 'движение_NOUN']

G = nx.Graph()
di = {}
for i in arr:
    x = i.find('_NOUN')
    di[i] = i[0:x]
    G.add_node(di[i])

for i in arr:
    for j in arr:
        if i < j:
            #print(di[i] + ' ' + di[j] + ' ' + str(model.similarity(i, j)))
            if model.similarity(i, j) > 0.2:
                G.add_edge(di[i], di[j])

print("радиус графа: " + str(nx.radius(G)))

print("5 самых центральных вершин:")
deg = nx.degree_centrality(G)
i = 0
for nodeid in sorted(deg, key=deg.get, reverse=True):
    if i < 5:
        print(nodeid)
        i += 1

print("плотность графа: " + str(nx.density(G)))

nx.write_gexf(G, 'graph_file.gexf')

pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='red', node_size=50) 
nx.draw_networkx_edges(G, pos, edge_color='yellow')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='Arial')
plt.axis('off') 
plt.show()

