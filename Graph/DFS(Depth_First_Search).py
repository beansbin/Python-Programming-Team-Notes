# DFS(Depth First Search), 깊이 우선 탐색
# 다른 경로로 탐색하다가 특정 상황에 최대한 깊숙히 들어가 탐색하는 알고리즘, 멀리 있는 노드 우선 탐색
# 스택 이용 -> 재귀 함수로 구현
# 참고 코드 : 나동빈 저 이코테 교재


# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드에 방문 표시
    visited[v] = True
    print(v, end=" ")

    # 현재 노드와 연결된 노드들을 차례로 방문(재귀)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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
dfs(graph, 1, visited)