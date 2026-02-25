def A(graph, h, start, goal):
    open_list = [start]
    closed = []
    g = [float('inf')] * len(graph)
    parent = [-1] * len(graph)
    g[start] = 0

    while open_list:
        current = min(open_list, key=lambda x: g[x] + h[x])

        if current == goal:
            path = []
            while current != -1:
                path.append(current)
                current = parent[current]
            return path[::-1]

        open_list.remove(current)
        closed.append(current)

        for neighbor, cost in graph[current]:
            if neighbor in closed:
                continue

            temp = g[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif temp >= g[neighbor]:
                continue

            parent[neighbor] = current
            g[neighbor] = temp

    return None
