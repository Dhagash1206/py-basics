import heapq

#create node

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


cities = [
    "Chicago", "Detroit", "Cleveland", "Buffalo",
    "Pittsburgh", "Columbus", "Indianapolis",
    "Syracuse", "Boston", "New York",
    "Philadelphia", "Baltimore", "Providence", "Portland"
]

graph = {city: [] for city in cities}

def add_edge(a, b, cost):
    graph[a].append((b, cost))
    graph[b].append((a, cost))


add_edge("Chicago","Detroit",283)
add_edge("Chicago","Indianapolis",182)
add_edge("Detroit","Cleveland",169)
add_edge("Detroit","Buffalo",256)
add_edge("Cleveland","Pittsburgh",134)
add_edge("Cleveland","Columbus",144)
add_edge("Buffalo","Syracuse",150)
add_edge("Pittsburgh","Philadelphia",305)
add_edge("Columbus","Pittsburgh",185)
add_edge("Columbus","Indianapolis",176)
add_edge("Syracuse","Boston",312)
add_edge("Boston","Providence",50)
add_edge("Providence","New York",181)
add_edge("New York","Philadelphia",97)
add_edge("Philadelphia","Baltimore",101)
add_edge("Boston","Portland",107)


path, cost = best_first_search("Chicago", "Boston", graph)

print("Path:", path)
print("Cost:", cost)
