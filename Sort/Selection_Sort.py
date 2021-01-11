# 선택 정렬(Selectio Sort)
# 가장 원시적인 방법으로, 매번 가장 작은 것을 선택해 앞에서부터 차례로 정렬
# 참고 코드 : 나동빈 저 이코테 교재

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

print(array)

