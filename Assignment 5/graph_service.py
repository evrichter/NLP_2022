import networkx as nx
import matplotlib.pyplot as plt

def plot_network(kg_df):
    Graph=nx.from_pandas_edgelist(kg_df[kg_df['edge']=="locate in"], "source", "target", 
                          edge_attr=True, create_using=nx.MultiDiGraph())

    plt.figure(figsize=(12,12))
    pos = nx.spring_layout(Graph, k = 0.5)
    nx.draw(Graph, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos = pos)
    plt.show()