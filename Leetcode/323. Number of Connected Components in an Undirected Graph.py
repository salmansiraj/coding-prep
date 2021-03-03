def countComponents(self, n: int, edges: List[List[int]]) -> int:
    if n <= 1:
        return n
    connected = 0
    graph = defaultdict(list)

    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)

    seen_nodes = set()

    def search(node):
        seen_nodes.add(node)
        for cur_nei in graph[node]:
            if cur_nei not in seen_nodes:
                search(cur_nei)

    for number in range(n):
        if number not in seen_nodes:
            search(number)
            connected += 1

    return connected
