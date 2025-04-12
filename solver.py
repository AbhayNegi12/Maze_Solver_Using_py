import heapq

def dijkstra(maze, cell_numbers, start, end):
    rows, cols = len(maze), len(maze[0])
    heap = [(cell_numbers[start], start)]
    distances = {start: cell_numbers[start]}
    predecessors = {}

    while heap:
        cost, current = heapq.heappop(heap)
        if current == end:
            break

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and not maze[nr][nc]:
                new_cost = cost + cell_numbers[neighbor]
                if neighbor not in distances or new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    predecessors[neighbor] = current
                    heapq.heappush(heap, (new_cost, neighbor))

    path = []
    node = end
    while node in predecessors:
        path.append(node)
        node = predecessors[node]
    path.append(start)
    path.reverse()
    return path

def calculate_path_cost(path, cell_numbers):
    return sum(cell_numbers.get(pos, 0) for pos in path)

def print_path_with_cost(path, cell_numbers, label):
    cost_parts = [str(cell_numbers[pos]) for pos in path]
    total = sum(cell_numbers[pos] for pos in path)
    print(f"{label} Path: {' + '.join(cost_parts)} = {total}")
