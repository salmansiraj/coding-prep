from typing import Collection


from collections import deque


def bfs(graph, root):
    visited = set()
    queue = deque()
    queue.append([root])

    while len(queue) > 0:
        currNode = queue.popleft()
        for neighbor in graph[currNode]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
