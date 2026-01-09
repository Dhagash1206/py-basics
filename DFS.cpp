
cities = [
    "Syracuse", "Buffalo", "Detroit", "Chicago", "Cleveland",
    "Columbus", "Indianapolis", "Pittsburgh",
    "Baltimore", "Philadelphia", "New York"
]

city_count = 11

graph = [
    # Syr Buf Det Chi Cle Col Ind Pit Bal Phi NY
    [0, 150, 0, 0, 0, 0, 0, 253, 0, 0, 254],     # Syracuse
    [150, 0, 256, 0, 189, 0, 0, 0, 0, 0, 0],     # Buffalo
    [0, 256, 0, 283, 169, 0, 0, 0, 0, 0, 0],     # Detroit
    [0, 0, 283, 0, 345, 0, 182, 0, 0, 0, 0],     # Chicago
    [0, 189, 169, 345, 0, 144, 0, 134, 0, 0, 0], # Cleveland
    [0, 0, 0, 0, 144, 0, 176, 185, 0, 0, 0],     # Columbus
    [0, 0, 0, 182, 0, 176, 0, 0, 0, 0, 0],       # Indianapolis
    [253, 0, 0, 0, 134, 185, 0, 0, 247, 305, 0], # Pittsburgh
    [0, 0, 0, 0, 0, 0, 0, 247, 0, 101, 0],       # Baltimore
    [0, 0, 0, 0, 0, 0, 0, 305, 101, 0, 97],      # Philadelphia
    [254, 0, 0, 0, 0, 0, 0, 0, 0, 97, 0]         # New York
]

MAX_PATH = 20

def dfs(current, goal, visited, path, cost):
    visited[current] = True
    path.append(current)

    if current == goal:
        print(" -> ".join(cities[i] for i in path) + f" | Cost: {cost}")
    else:
        for i in range(city_count):
            w = graph[current][i]
            if w != 0 and not visited[i]:
                dfs(i, goal, visited, path, cost + w)

    visited[current] = False
    path.pop()

from collections import deque
def bfs(start, goal):
    queue = deque()
    start_node = {
        "city": start,
        "path": [start],
        "cost": 0,
        "visited": [False]*city_count
    }
    start_node["visited"][start] = True
    queue.append(start_node)

    while queue:
        curr = queue.popleft()
        if curr["city"] == goal:
            print(" -> ".join(cities[i] for i in curr["path"]) + f" | Cost: {curr['cost']}")
            continue

        for i in range(city_count):
            w = graph[curr["city"]][i]
            if w != 0 and not curr["visited"][i]:
                next_node = {
                    "city": i,
                    "path": curr["path"] + [i],
                    "cost": curr["cost"] + w,
                    "visited": curr["visited"][:]
                }
                next_node["visited"][i] = True
                queue.append(next_node)

if __name__ == "__main__":
    start = 0  # Syracuse
    goal = 3   # Chicago

    print("DFS Results:")
    dfs(start, goal, [False]*city_count, [], 0)

    print("\nBFS Results:")
    bfs(start, goal)

// -----------------------------
// Adjacency matrix (weights)
// 0 means no direct edge
// -----------------------------
int graph[11][11] = {
    // Syr Buf Det Chi Cle Col Ind Pit Bal Phi NY
    {0, 150, 0, 0, 0, 0, 0, 253, 0, 0, 254},     // Syracuse
    {150, 0, 256, 0, 189, 0, 0, 0, 0, 0, 0},     // Buffalo
    {0, 256, 0, 283, 169, 0, 0, 0, 0, 0, 0},     // Detroit
    {0, 0, 283, 0, 345, 0, 182, 0, 0, 0, 0},     // Chicago
    {0, 189, 169, 345, 0, 144, 0, 134, 0, 0, 0}, // Cleveland
    {0, 0, 0, 0, 144, 0, 176, 185, 0, 0, 0},     // Columbus
    {0, 0, 0, 182, 0, 176, 0, 0, 0, 0, 0},       // Indianapolis
    {253, 0, 0, 0, 134, 185, 0, 0, 247, 305, 0}, // Pittsburgh
    {0, 0, 0, 0, 0, 0, 0, 247, 0, 101, 0},       // Baltimore
    {0, 0, 0, 0, 0, 0, 0, 305, 101, 0, 97},      // Philadelphia
    {254, 0, 0, 0, 0, 0, 0, 0, 0, 97, 0}         // New York
};

// -----------------------------
// DFS implementation
// -----------------------------
int visited[11];
int path[MAX_PATH];

void dfs(int current, int goal, int pathIndex, int cost)
{
    visited[current] = 1;
    path[pathIndex] = current;

    if (current == goal)
    {
        for (int i = 0; i <= pathIndex; i++)
        {
            printf("%s", cities[path[i]]);
            if (i != pathIndex)
                printf(" -> ");
        }
        printf(" | Cost: %d\n", cost);
    }
    else
    {
        for (int i = 0; i < cityCount; i++)
        {
            if (graph[current][i] != 0 && !visited[i])
            {
                dfs(i, goal, pathIndex + 1,
                    cost + graph[current][i]);
            }
        }
    }

    visited[current] = 0; // backtrack
}

// -----------------------------
// BFS implementation
// -----------------------------
typedef struct
{
    int city;
    int path[MAX_PATH];
    int pathLen;
    int cost;
    int visited[11];
} Node;

void bfs(int start, int goal)
{
    Node queue[1000];
    int front = 0, rear = 0;

    Node startNode = {start, {start}, 1, 0, {0}};
    startNode.visited[start] = 1;
    queue[rear++] = startNode;

    while (front < rear)
    {
        Node curr = queue[front++];

        if (curr.city == goal)
        {
            for (int i = 0; i < curr.pathLen; i++)
            {
                printf("%s", cities[curr.path[i]]);
                if (i != curr.pathLen - 1)
                    printf(" -> ");
            }
            printf(" | Cost: %d\n", curr.cost);
            continue;
        }

        for (int i = 0; i < cityCount; i++)
        {
            if (graph[curr.city][i] != 0 && !curr.visited[i])
            {
                Node next = curr;
                next.city = i;
                next.path[next.pathLen++] = i;
                next.cost += graph[curr.city][i];
                next.visited[i] = 1;
                queue[rear++] = next;
            }
        }
    }
}

// -----------------------------
// Main
// -----------------------------
int main()
{
    int start = 0; // Syracuse
    int goal = 3;  // Chicago

    printf("DFS Results:\n");
    dfs(start, goal, 0, 0);

    printf("\nBFS Results:\n");
    bfs(start, goal);

    return 0;
}