import heapq
import random

DIFFICULTY = {'easy': (5, 0.5), 'medium': (10, 0.45), 'hard': (16, 0.4)}

def generate_maze(rows, cols, wall_prob):
    for _ in range(50):
        maze = [[0 if random.random() > wall_prob else 1 for _ in range(cols)] for _ in range(rows)]
        maze[0][0] = maze[rows-1][cols-1] = 0
        if dijkstra(maze, (0, 0), (rows-1, cols-1)):
            return maze
    exit("Failed to generate a valid maze.")

def dijkstra(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    pq, distances, parent = [(0, start)], {start: 0}, {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        cost, (r, c) = heapq.heappop(pq)
        if (r, c) == end:
            path = []
            while (r, c) in parent:
                path.append((r, c))
                r, c = parent[(r, c)]
            path.append(start)
            return path[::-1]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                new_cost = cost + 1
                if (nr, nc) not in distances or new_cost < distances[(nr, nc)]:
                    distances[(nr, nc)] = new_cost
                    heapq.heappush(pq, (new_cost, (nr, nc)))
                    parent[(nr, nc)] = (r, c)
    return None
