# Búsqueda en profundidad:
# •	Dado un grafo no dirigido, implementa una función que realice una búsqueda en profundidad
# desde un nodo de inicio dado y devuelva la lista de nodos visitados en orden.
# •	Implementa una función que determine si hay un camino entre dos nodos en un grafo utilizando
# la búsqueda en profundidad.

def dfs(graph, start):
    visited = set()  # Conjunto para almacenar los nodos visitados
    stack = [start]  # Pila para almacenar los nodos por visitar
    visited_order = []  # Lista para almacenar el orden de visita de los nodos

    while stack:
        node = stack.pop()  # Extraer el último nodo agregado a la pila

        if node not in visited:
            visited.add(node)
            visited_order.append(node)

            # Agregar los vecinos no visitados a la pila
            neighbors = graph[node]
            stack.extend([neighbor for neighbor in neighbors if neighbor not in visited])

    return visited_order

def has_path(graph, start, end):
    visited = set()  # Conjunto para almacenar los nodos visitados
    stack = [start]  # Pila para almacenar los nodos por visitar

    while stack:
        node = stack.pop()  # Extraer el último nodo agregado a la pila

        if node == end:
            return True

        if node not in visited:
            visited.add(node)

            # Agregar los vecinos no visitados a la pila
            neighbors = graph[node]
            stack.extend([neighbor for neighbor in neighbors if neighbor not in visited])

    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
visited_nodes = dfs(graph, start_node)
print("Nodos visitados en orden:", visited_nodes)

node1 = 'A'
node2 = 'F'
path_exists = has_path(graph, node1, node2)
if path_exists:
    print("Hay un camino entre", node1, "y", node2)
else:
    print("No hay un camino entre", node1, "y", node2)

