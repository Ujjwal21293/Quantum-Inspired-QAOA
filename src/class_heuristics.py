import networkx as nx

def dijkstra_path(graph, start, end):
    return nx.dijkstra_path(graph, source=start, target=end, weight='weight')

def a_star_path(graph, start, end):
    return nx.astar_path(graph, start, end, heuristic=lambda u, v: 1, weight='weight')
