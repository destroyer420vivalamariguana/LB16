import networkx as nx
import matplotlib.pyplot as plt
import math

def dijkstra(graph, start):
    # Inicializar las estructuras de datos
    distance = {node: math.inf for node in graph}
    distance[start] = 0
    visited = set()

    while len(visited) < len(graph):
        # Encontrar el nodo con la distancia mínima
        min_distance = math.inf
        min_node = None
        for node in graph:
            if node not in visited and distance[node] < min_distance:
                min_distance = distance[node]
                min_node = node

        if min_node is None:
            break

        visited.add(min_node)

        # Actualizar las distancias de los nodos vecinos
        for neighbor, weight in graph[min_node].items():
            new_distance = distance[min_node] + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance

    return distance

def draw_graph(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', width=1, alpha=0.7)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

# Grafo de ejemplo
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 1},
    'C': {'A': 2, 'F': 12},
    'D': {'B': 5},
    'E': {'B': 1, 'F': 3},
    'F': {'C': 12, 'E': 3}
}

# Nodo de inicio
start_node = 'A'

# Ejecutar el algoritmo de Dijkstra
distances = dijkstra(graph, start_node)
print(distances)

# Generar el gráfico del grafo
draw_graph(graph)