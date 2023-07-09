import networkx as nx
import matplotlib.pyplot as plt


def dfs(graph, start):
    visited = set()  # Conjunto para almacenar los nodos visitados
    stack = [start]  # Pila para almacenar los nodos por visitar

    while stack:
        node = stack.pop()  # Extraer el último nodo agregado a la pila

        if node not in visited:
            visited.add(node)
            print(node)  # Imprimir el nodo visitado

            # Agregar los vecinos no visitados a la pila
            neighbors = graph[node]
            stack.extend([neighbor for neighbor in neighbors if neighbor not in visited])


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

# Realizar la búsqueda en profundidad desde el nodo 'A'
dfs(graph, 'A')

# Generar el gráfico del grafo
draw_graph(graph)