import heapq

def dijkstra(graph, start):
    # Dictionary to store the shortest distance from the start node to each node
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    # Priority queue to store (distance, node) tuples
    priority_queue = [(0, start)]

    # Dictionary to store the shortest path to each node
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if a shorter path to the node has already been found
        if current_distance > shortest_distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances, previous_nodes

def reconstruct_path(previous_nodes, start, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path if path[0] == start else []

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

start_node = 'A'
target_node = 'D'

shortest_distances, previous_nodes = dijkstra(graph, start_node)
shortest_path = reconstruct_path(previous_nodes, start_node, target_node)

print("Shortest distances from node", start_node, ":", shortest_distances)
print("Shortest path from", start_node, "to", target_node, ":", shortest_path)
