# 코드는 지저분하지만
# 성공은 했다

from collections import deque

n, m = list(map(int, input().split()))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

start = [0, 0]
visited = [[False for _ in range(m)] for _ in range(n)]
queue = deque([start])
# visited[start[0]][start[1]] = True

graph2 = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
for i in range(n):
    for j in range(m):
        if (visited[i][j] == False and graph[i][j] == 0) or (i == 0 and j == 0):
            if not (i == 0 and j == 0):
                queue.append([i, j])
            visited[i][j] = True
            while queue:
                v = queue.popleft()
                # print(v, end=" ")

                start[0] = v[0]
                start[1] = v[1]

                for k in range(4):
                    if start[0] + dx[0] >= 0 and graph[start[0] + dx[0]][start[1] + dy[0]] == 0 and \
                            visited[start[0] + dx[0]][start[1] + dy[0]] == False:  # 위
                        queue.append([start[0] + dx[0], start[1] + dy[0]])
                        visited[start[0] + dx[0]][start[1] + dy[0]] = True
                    if start[0] + dx[2] < n and graph[start[0] + dx[2]][start[1] + dy[2]] == 0 and \
                            visited[start[0] + dx[2]][start[1] + dy[2]] == False:  # 아래
                        queue.append([start[0] + dx[2], start[1] + dy[2]])
                        visited[start[0] + dx[2]][start[1] + dy[2]] = True
                    if start[1] + dy[1] < m and graph[start[0] + dx[1]][start[1] + dy[1]] == 0 and \
                            visited[start[0] + dx[1]][start[1] + dy[1]] == False:  # 오른쪽
                        queue.append([start[0] + dx[1], start[1] + dy[1]])
                        visited[start[0] + dx[1]][start[1] + dy[1]] = True
                    if start[1] + dy[3] >= 0 and graph[start[0] + dx[3]][start[1] + dy[3]] == 0 and \
                            visited[start[0] + dx[3]][start[1] + dy[3]] == False:  # 왼쪽
                        queue.append([start[0] + dx[3], start[1] + dy[3]])
                        visited[start[0] + dx[3]][start[1] + dy[3]] = True

            # print()
            count += 1
print(count)





