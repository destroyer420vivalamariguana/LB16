import networkx as nx
import matplotlib.pyplot as plt


def bfs(graph, start):
    visited = set()  # Conjunto para almacenar los nodos visitados
    queue = [start]  # Cola para almacenar los nodos por visitar

    while queue:
        node = queue.pop(0)  # Extraer el primer nodo agregado a la cola

        if node not in visited:
            visited.add(node)
            print(node)  # Imprimir el nodo visitado

            # Agregar los vecinos no visitados a la cola
            neighbors = graph[node]
            queue.extend([neighbor for neighbor in neighbors if neighbor not in visited])


def draw_graph(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', width=1, alpha=0.7)
    plt.show()


# Grafo de ejemplo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Realizar la búsqueda en amplitud desde el nodo 'A'
bfs(graph, 'A')

# Generar el gráfico del grafo
draw_graph(graph)