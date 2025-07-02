from collections import deque

# Romania map represented as a graph (adjacency list)
romania_map = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu'],
    'Giurgiu': ['Bucharest']
}

def bfs(start, goal):
    # Frontier queue with path stored
    frontier = deque([[start]])
    explored = set()

    while frontier:
        path = frontier.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in explored:
            explored.add(node)

            for neighbor in romania_map.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                frontier.append(new_path)

    return None  # No path found

# Run BFS from Arad to Bucharest
path = bfs('Arad', 'Bucharest')
print("Path from Arad to Bucharest using BFS:")
print(" -> ".join(path))
