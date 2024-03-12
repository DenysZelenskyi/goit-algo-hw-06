from collections import deque


def bfs_iterative(graph, start_vertex, end_vertex):
    visited = set()
    queue = deque([(start_vertex, [start_vertex])])

    while queue:
        vertex, path = queue.popleft()
        if vertex == end_vertex:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for next_vertex in graph[vertex]:
                if next_vertex not in visited:
                    queue.append((next_vertex, path + [next_vertex]))
    return visited