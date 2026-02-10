import heapq

class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def best_first_search(start, goal, graph):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0)
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.state == goal:
            return get_path(current), current.cost

        if current.state in closed_set:
            continue

        closed_set.add(current.state)

        for neighbor, step_cost in graph[current.state]:
            
            if neighbor not in closed_set:
                child = Node(
                    neighbor,
                    current,
                    current.cost + step_cost
                )
                heapq.heappush(open_list, child)

    return None, float("inf")


def get_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


# Example weighted graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 3)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

path, cost = best_first_search('A', 'F', graph)
print("Path:", path)
print("Cost:", cost)
