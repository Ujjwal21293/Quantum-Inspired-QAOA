import sys
import os

# Dynamically add src/ to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from graph_load import load_graph
from qaoa_simulator import QAOASimulator
from class_heuristics import dijkstra_path
import matplotlib.pyplot as plt
import time

G = load_graph('sample_graph.json')
start, end = 'A', 'G'

# QAOA
qaoa = QAOASimulator(G)
start_q = time.time()
q_path, q_cost = qaoa.optimize(start, end)
end_q = time.time()

# Dijkstra
start_d = time.time()
d_path = dijkstra_path(G, start, end)
d_cost = sum(G[d_path[i]][d_path[i+1]]['weight'] for i in range(len(d_path)-1))
end_d = time.time()

print(f"QAOA Path: {q_path} | Cost: {q_cost} | Time: {end_q - start_q:.4f}s")
print(f"Dijkstra Path: {d_path} | Cost: {d_cost} | Time: {end_d - start_d:.4f}s")

# Plot
plt.bar(['QAOA', 'Dijkstra'], [q_cost, d_cost], color=['blue', 'orange'])
plt.title("Route Cost Comparison")
plt.ylabel("Total Cost")
plt.savefig("performance_comparison.png")
plt.show()
