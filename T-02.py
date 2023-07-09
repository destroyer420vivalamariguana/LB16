# Búsqueda en amplitud:
# •	Dado un grafo no dirigido, implementa una función que realice una búsqueda en
# amplitud desde un nodo de inicio dado y devuelva la lista de nodos visitados en orden.
# •	Implementa una función que encuentre el camino más corto entre dos nodos en un grafo
# utilizando la búsqueda en amplitud.
from collections import deque
def bfs(graph, start):
    visited = set()  # Conjunto para almacenar los nodos visitados
    queue = deque([start])  # Cola para almacenar los nodos por visitar
    visited_order = []  # Lista para almacenar el orden de visita de los nodos
    while queue:
        node = queue.popleft()  # Extraer el primer nodo agregado a la cola
        if node not in visited:
            visited.add(node)
            visited_order.append(node)
            # Agregar los vecinos no visitados a la cola
            neighbors = graph[node]
            queue.extend([neighbor for neighbor in neighbors if neighbor not in visited])

    return visited_order

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])  # Cola para almacenar los nodos por visitar y sus respectivos caminos
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return None  # No se encontró un camino entre los nodos

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
visited_nodes = bfs(graph, start_node)
print("Nodos visitados en orden:", visited_nodes)

node1 = 'A'
node2 = 'F'
shortest_path = shortest_path(graph, node1, node2)
if shortest_path:
    print("Camino más corto entre", node1, "y", node2, ":", shortest_path)
else:
    print("No se encontró un camino entre", node1, "y", node2)
