import heapq

# Romania map with distances
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)]
}

def ucs(start, goal):
    # Priority queue: (total_cost, path)
    frontier = [(0, [start])]
    explored = set()

    while frontier:
        cost_so_far, path = heapq.heappop(frontier)
        node = path[-1]

        if node == goal:
            return path, cost_so_far

        if node not in explored:
            explored.add(node)

            for neighbor, step_cost in romania_map.get(node, []):
                if neighbor not in explored:
                    new_path = list(path)
                    new_path.append(neighbor)
                    heapq.heappush(frontier, (cost_so_far + step_cost, new_path))

    return None, float('inf')  # If no path found

# Run UCS from Arad to Bucharest
path, cost = ucs('Arad', 'Bucharest')
print("Least-cost path from Arad to Bucharest using UCS:")
print(" -> ".join(path))
print("Total cost:", cost)
