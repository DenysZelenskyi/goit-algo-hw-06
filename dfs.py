from collections import deque


def dfs_iterative(graph, start_vertex, end_vertex):
    visited = set()
    stack = [(start_vertex, [start_vertex])]
    while stack:
        vertex, path = stack.pop()
        if vertex == end_vertex:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for next_vertex in reversed(graph[vertex]):
                if next_vertex not in visited:
                    stack.append((next_vertex, path + [next_vertex]))
    return None