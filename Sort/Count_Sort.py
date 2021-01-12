# 계수 정렬(Count Sort)
# 데이터의 크기가 정해져있고 정수일 때 가장 빠르게 동작하는 알고리즘
# 데이터의 범위만큼 리스트를 선언한 뒤 리스트에 데이터 갯수를 카운팅
# 참고 : 나동빈 저 이코테

arr = [7, 5, 0, 9, 3, 4, 8, 2, 6, 1, 1, 3, 4]

# 모든 범위를 포함하는 리스트(0으로 초기화)
count = [0] * (max(arr)+1)

for i in range(len(arr)):
  count[arr[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
  for j in range(count[i]):
    print(i, end=" ")