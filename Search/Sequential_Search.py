# 순차 탐색(Sequential_Search)
# 리스트 안에 있는 특정 데이터를 찾기 위해 앞에서부터 차례대로 확인하는 방법
# 참고 : 나동빈 저 이코테

def sequential_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스 + 1)

input_data = input().split()
n = int(input_data[0])
target = int(input_data[1])

arr = input().split()

print(sequential_search(n, target, arr))