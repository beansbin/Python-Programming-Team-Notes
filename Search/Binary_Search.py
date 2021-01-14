# 이진 탐색(Binary_Search)
# 시작적, 중간점, 끝점을 가지고 범위를 반씩 줄여가며 원하는 데이터를 찾는 방식
# 참고 : 나동빈 저 이코테

# 반복문 사용
def binary_search_iter(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2 # 중간점 인덱스

    if arr[mid] == target: # 데이터를 찾은 경우 중간점 인덱스 반환
        return mid
    elif arr[mid] > target: # 더 큰 경우 왼쪽 확인
        end = mid -1
    elif arr[mid] < target: # 더 작은 경우 오른쪽 확인
        start = mid + 1
    return None

# 재귀 함수 사용
def binary_search_recur(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # 중간점 인덱스

        if arr[mid] == target: # 데이터를 찾은 경우 중간점 인덱스 반환
            return mid
        elif arr[mid] > target:  # 더 큰 경우 왼쪽 확인
            return binary_search_iter(arr, target, start, mid - 1)
        elif arr[mid] < target:  # 더 작은 경우 오른쪽 확인
            return binary_search_iter(arr, target, mid + 1, end)


n, target = list(map(int, input().split())) # 원소 개수와 찾으려는 데이터
arr = list(map(int, input().split())) # 리스트 입력

result = binary_search_recur()
result2 = binary_search_iter()
if result != None:
    print(result)
if result2 != None:
    print(result2)

