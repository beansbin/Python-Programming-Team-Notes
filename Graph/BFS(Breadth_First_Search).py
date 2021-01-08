# BFS(Breadth First Search), 너비 우선 탐색
# 가까이 있는 노드를 우선으로 탐색하는 방식, 큐 이용
# 참고 코드 : 나동빈 저 이코테 교재

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # deque를 이용한 큐 구현
    queue = deque([start])
    # 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 노를 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")

        # 해당 노드와 연결된 노드 중 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 그래프를 2차원 인접 리스트로 표현
graph = [
    [],
    [2, 3, 8], # 1번 노드에 연결된 노드들
    [1, 7], # 2번 노드에 연결된 노드들
    [1, 4, 5], # ...
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)