import json
import networkx as nx

def load_graph(path):
    with open(path, 'r') as f:
        data = json.load(f)

    G = nx.Graph()
    for edge in data["edges"]:
        G.add_edge(edge["from"], edge["to"], weight=edge["weight"])
    return G
