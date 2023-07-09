# Algoritmo de Dijkstra:
# •	Dado un grafo ponderado dirigido, implementa el algoritmo de Dijkstra para encontrar la distancia más
# corta desde un nodo de inicio dado a todos los demás nodos. Devuelve las distancias más cortas como un diccionario.
# •	Modifica la implementación de Dijkstra para que también devuelva el camino más corto desde el nodo de inicio
# hasta cada uno de los otros nodos.
import math
import heapq

def dijkstra(graph, start):
    distances = {node: math.inf for node in graph}  # Distancias iniciales a infinito
    distances[start] = 0  # Distancia al nodo de inicio es 0
    visited = set()  # Conjunto para almacenar los nodos visitados
    pq = [(0, start)]  # Cola de prioridad para almacenar los nodos por visitar y sus distancias
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def dijkstra_with_path(graph, start):
    distances = {node: math.inf for node in graph}  # Distancias iniciales a infinito
    distances[start] = 0  # Distancia al nodo de inicio es 0
    visited = set()  # Conjunto para almacenar los nodos visitados
    pq = [(0, start)]  # Cola de prioridad para almacenar los nodos por visitar y sus distancias
    paths = {node: [] for node in graph}  # Caminos iniciales vacíos
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [current_node]
                heapq.heappush(pq, (distance, neighbor))
    return distances, paths

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print("Distancias más cortas:", distances)

distances_with_paths, paths = dijkstra_with_path(graph, start_node)
print("Distancias más cortas:", distances_with_paths)
print("Caminos más cortos:")
for node, path in paths.items():
    print(f"{node}: {path + [node]}")

