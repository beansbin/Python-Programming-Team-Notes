# 실패

from collections import deque

n, m = list(map(int, input().split()))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

count = 0


def bfs(graph, x, y, visited):
    count = 0
    visit = []
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        v = queue.popleft()
        print(v)
        print(queue)
        x = v[0]
        y = v[1]

        if x >= 0 and x < n and y >= 0 and y < n:
            if x - 1 >= 0:
                if graph[x - 1][y] == 1:  # 위
                    queue.append((x - 1, y))
                    visited[x - 1][y] = True
                    count += 1
                    if x - 1 == n and y == m:
                        visit.append(count)
                        count = 0
                        continue

            if x + 1 < m:
                if graph[x + 1][y] == 1:  # 아래
                    queue.append((x + 1, y))
                    visited[x + 1][y] = True
                    count += 1
                    if x + 1 == n and y == m:
                        visit.append(count)
                        count = 0
                        continue

            if y - 1 >= 0:
                if graph[x][y - 1] == 1:  # 왼쪽
                    queue.append((x, y - 1))
                    visited[x][y - 1] = True
                    count += 1
                    if x == n and y - 1 == m:
                        visit.append(count)
                        count = 0
                        continue

            if y + 1 < n:
                if graph[x][y + 1] == 1:  # 오른쪽
                    queue.append((x, y + 1))
                    visited[x][y + 1] = True
                    count += 1
                    if x == n and y + 1 == m:
                        visit.append(count)
                        count = 0
                        continue

    return visit


print(bfs(graph, 0, 0, visited))
print(visited)










