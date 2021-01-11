n, m, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort(reverse=True)

result = 0
count = 0

for i in range(m):
    if count < 3:
        result += arr[0]
        count += 1
    elif count == 3:
        count = 0
        result += arr[1]

print(result)
