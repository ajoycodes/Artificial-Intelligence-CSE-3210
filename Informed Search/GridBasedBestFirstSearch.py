import heapq


def manhattan_distance(cell, goal):
    r1, c1 = cell
    r2, c2 = goal
    return abs(r1 - r2) + abs(c1 - c2)


def greedy_f(cell, goal, path_cost):
    return manhattan_distance(cell, goal)


def astar_f(cell, goal, path_cost):
    return path_cost + manhattan_distance(cell, goal)


def get_neighbors(cell, grid):
    r, c = cell
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dr, dc in moves:
        nr, nc = r + dr, c + dc

        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != -1:
                neighbors.append((nr, nc))

    return neighbors


def reconstruct_path(parent, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()
    return path


def best_first_search(grid, start, goal, F):
    frontier = []
    heapq.heappush(frontier, (F(start, goal, 0), start))

    explored = set()
    parent = {start: None}
    path_cost = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            return reconstruct_path(parent, start, goal)

        explored.add(current)

        for cell in get_neighbors(current, grid):
            new_cost = path_cost[current] + 1

            if cell not in explored:
                parent[cell] = current
                path_cost[cell] = new_cost

                f = F(cell, goal, new_cost)
                heapq.heappush(frontier, (f, cell))

    return None