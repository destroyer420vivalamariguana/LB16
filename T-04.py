# Algoritmo de Bellman-Ford:
# •	Dado un grafo ponderado dirigido, implementa el algoritmo de Bellman-Ford para encontrar la distancia más corta
# desde un nodo de inicio dado a todos los demás nodos. Asegúrate de manejar correctamente los ciclos de costo negativo.
# •	Modifica la implementación de Bellman-Ford para que también devuelva el
# camino más corto desde el nodo de inicio hasta cada uno de los otros nodos.
import math
def bellman_ford(graph, start):
    distances = {node: math.inf for node in graph}  # Distancias iniciales a infinito
    distances[start] = 0  # Distancia al nodo de inicio es 0
    # Realizar el proceso de relajación de las aristas V-1 veces
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                distance = distances[node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
    # Verificar si hay ciclos de costo negativo
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("El grafo contiene un ciclo de costo negativo")
    return distances

def bellman_ford_with_path(graph, start):
    distances = {node: math.inf for node in graph}  # Distancias iniciales a infinito
    distances[start] = 0  # Distancia al nodo de inicio es 0
    paths = {node: [] for node in graph}  # Caminos iniciales vacíos
    # Realizar el proceso de relajación de las aristas V-1 veces
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                distance = distances[node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[node] + [node]
    # Verificar si hay ciclos de costo negativo
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("El grafo contiene un ciclo de costo negativo")
    # Agregar el último nodo en el camino más corto
    for node in graph:
        paths[node].append(node)
    return distances, paths

graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

start_node = 'A'
distances = bellman_ford(graph, start_node)
print("Distancias más cortas:", distances)

distances_with_paths, paths = bellman_ford_with_path(graph, start_node)
print("Distancias más cortas:", distances_with_paths)
print("Caminos más cortos:")
for node, path in paths.items():
    print(f"{node}: {path}")