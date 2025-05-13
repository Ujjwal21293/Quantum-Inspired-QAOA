import sys
import os

# Dynamically add src/ to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from qaoa_simulator import QAOASimulator
import networkx as nx

def test_qaoa_basic():
    G = nx.path_graph(5)
    nx.set_edge_attributes(G, 1, 'weight')
    qaoa = QAOASimulator(G)
    path, cost = qaoa.optimize(0, 4)
    assert path[0] == 0 and path[-1] == 4
    assert cost <= 4
