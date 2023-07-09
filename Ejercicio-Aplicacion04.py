import networkx as nx
import matplotlib.pyplot as plt
import math

def bellman_ford(graph, start):
    # Inicializar las distancias a infinito excepto para el nodo de inicio
    distance = {node: math.inf for node in graph}
    distance[start] = 0

    # Realizar el proceso de relajación de las aristas V-1 veces
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                new_distance = distance[node] + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance

    # Verificar si hay ciclos de costo negativo
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distance[node] + weight < distance[neighbor]:
                raise ValueError("El grafo contiene un ciclo de costo negativo")

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
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

# Nodo de inicio
start_node = 'A'

# Ejecutar el algoritmo de Bellman-Ford
distances = bellman_ford(graph, start_node)
print(distances)

# Generar el gráfico del grafo
draw_graph(graph)