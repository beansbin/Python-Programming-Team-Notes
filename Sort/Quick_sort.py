# 퀵 정렬(Quick sort)
# 빠른 속도로 일반적인 상황에 가장 많이 사용되는 알고리즘
# 피벗을 설정해 큰 수와 작은 수를 교환해 리스트를 반으로 나눈 후 재귀를 통해 정렬 수행
# 참고 : 나동빈 저 이코테

arr = [7, 5, 0, 9, 3, 4, 8, 2, 6, 1]


# 1. 전통적인 퀵 정렬
def quick_sort(arr, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:  # 엇갈린 경우 작은 데이터와 피벗 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:  # 엇갈리지 않은 경우 작은 데이터와 큰 데이터 교체
            arr[left], arr[right] = arr[right], arr[left]

    # 분할 이후 왼쪽, 오른쪽에서 각각 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


quick_sort(arr, 0, len(arr) - 1)
print(arr)

arr = [7, 5, 0, 9, 3, 4, 8, 2, 6, 1]


# 2. 파이썬 퀵 정렬
# 직관적이지만 피벗과 데이터 간 연산 횟수 증가
def quick_sort_python(arr):
    if len(arr) <= 1:  # 원소가 1개 이하인 경우 종료
        return arr

    pivot = arr[0]  # 피벗은 첫 번째 원소
    tail = arr[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽, 오른쪽에서 각각 정렬 수행 후 전체 리스트 반환
    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)


print(quick_sort_python(arr))
