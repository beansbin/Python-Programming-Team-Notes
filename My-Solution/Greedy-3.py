n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
    cards[i].sort()
    if cards[i][0] > result:
        result = cards[i][0]

print(result)
