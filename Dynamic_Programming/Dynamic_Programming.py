# 다이나믹 프로그래밍(Dynamic Programming)
# 조건 만족 시 사용 : 1. 큰 문제를 작게 나눌 수 있을 때 2. 작은 문제의 해답이 큰 문제의 풀이에 사용될 때
# 메모리 공간을 사용해 속도를 향상시키는 방법
# 참고 : 나동빈 저 이코테

# 일반적인 피보나치 함수 소스코드
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2) # 같은 함수가 중복 호출됨

print(fibo(4))


# 탑다운(Top-Down)방식 (재귀함수)
d = [0] * 100 # 메모이제이션을 위한 리스트

def fibo_t(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산했던 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo_t(x-1) + fibo_t(x-2)
    return d[x]

print(fibo_t(99))


# 보텀업(Bottom-Up) 방식 (반복문)
d = [0] * 100 # DP 테이블

d[1], d[2] = 1, 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
for i in d:
    print(i, end=" ")

