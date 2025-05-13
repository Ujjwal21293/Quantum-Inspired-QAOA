import numpy as np
import networkx as nx
import random

class QAOASimulator:
    def __init__(self, graph, p=3):
        self.graph = graph
        self.p = p
        self.nodes = list(graph.nodes)

    def cost_function(self, path):
        total_cost = 0
        for i in range(len(path) - 1):
            if self.graph.has_edge(path[i], path[i+1]):
                total_cost += self.graph[path[i]][path[i+1]]['weight']
            else:
                total_cost += 1000  # Heavy penalty for invalid path
        return total_cost

    def mixer(self, path):
        new_path = path[:]
        i, j = random.sample(range(len(path)), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        return new_path

    def optimize(self, start, end, iterations=100):
        best_path = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
        best_cost = self.cost_function(best_path)

        for _ in range(iterations):
            candidate = self.mixer(best_path)
            try:
                if nx.has_path(self.graph, candidate[0], candidate[-1]):
                    new_cost = self.cost_function(candidate)
                    if new_cost < best_cost:
                        best_path, best_cost = candidate, new_cost
            except nx.NetworkXNoPath:
                continue

        return best_path, best_cost
