import heapq
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("graph.png")
plt.imshow(img)
plt.axis("off")
plt.show()

graph = {
    "Chicago": {"Detroit":283, "Indianapolis":182, "Cleveland":345},
    "Detroit": {"Chicago":283, "Cleveland":169, "Buffalo":256},
    "Indianapolis": {"Chicago":182, "Columbus":176},
    "Columbus": {"Indianapolis":176, "Cleveland":144, "Pittsburgh":185},
    "Cleveland": {"Chicago":345, "Detroit":169, "Columbus":144, "Pittsburgh":134, "Buffalo":189},
    "Pittsburgh": {"Cleveland":134, "Columbus":185, "Buffalo":215, "Philadelphia":305, "Baltimore":247},
    "Buffalo": {"Detroit":256, "Cleveland":189, "Pittsburgh":215, "Syracuse":150},
    "Syracuse": {"Buffalo":150, "New York":254, "Philadelphia":253, "Boston":312},
    "Philadelphia": {"Pittsburgh":305, "Syracuse":253, "New York":97, "Baltimore":101},
    "Baltimore": {"Pittsburgh":247, "Philadelphia":101},
    "New York": {"Philadelphia":97, "Syracuse":254, "Boston":215, "Providence":181},
    "Providence": {"New York":181, "Boston":50},
    "Boston": {"New York":215, "Providence":50, "Syracuse":312, "Portland":107},
    "Portland": {"Boston":107}
}

def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

path, cost = uniform_cost_search(graph, "Chicago", "Portland")

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)
