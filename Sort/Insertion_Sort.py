# 삽임 정렬(Insertion Sort)
# 앞서 정렬되어있는 데이터들 중 적절한 위치에 현재 원소를 삽입
# 데이터가 거의 정렬되어 있는 경우 빠르게 동작(else: break)
# 참고 코드 : 나동빈 저 이코테 교재

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 한 칸씩 왼쪽으로 이동
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
    print(array)


print(array)

