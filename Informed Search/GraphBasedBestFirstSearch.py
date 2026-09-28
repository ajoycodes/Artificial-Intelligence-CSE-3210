import heapq

--

def heuristic(node, goal):
    h = {
        "S": 4,
        "A": 1,
        "B": 2,
        "G": 0
    }
    return h[node]


def greedy_f(node, goal, path_cost):
    return heuristic(node, goal)


def astar_f(node, goal, path_cost):
    return path_cost + heuristic(node, goal)


def reconstruct_path(parent, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    return path


def best_first_search(graph, start, goal, F):
    frontier = []

    f_value = F(start, goal, 0)
    heapq.heappush(frontier, (f_value, start))

    explored = set()
    parent = {start: None}
    path_cost = {start: 0}

    while frontier:
        dummy, current = heapq.heappop(frontier)

        if current == goal:
            final_path = reconstruct_path(parent, start, goal)
            final_cost = path_cost[current]
            return final_cost, final_path

        explored.add(current)

        for neighbor, cost in graph[current]:
            new_path_cost = path_cost[current] + cost

            if neighbor not in explored:
                parent[neighbor] = current
                path_cost[neighbor] = new_path_cost

                f_value = F(neighbor, goal, new_path_cost)
                heapq.heappush(frontier, (f_value, neighbor))

    return None




