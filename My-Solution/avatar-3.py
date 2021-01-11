location = input()
loc = [0, 0]
dict1 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
count = 0

loc[0] = dict1[location[0]]
loc[1] = int(location[1]) - 1

if loc[0] - 2 >= 0:  # 위
    if loc[1] - 1 >= 0:
        count += 1
    if loc[1] + 1 < 8:
        count += 1

if loc[0] + 2 < 8:  # 아래
    if loc[1] - 1 >= 0:
        count += 1
    if loc[1] + 1 < 8:
        count += 1

if loc[1] - 2 >= 0:  # 왼쪽
    if loc[0] - 1 >= 0:
        count += 1
    if loc[0] + 1 < 8:
        count += 1

if loc[1] + 2 < 8:  # 오른쪽
    if loc[1] - 1 >= 0:
        count += 1
    if loc[1] + 1 < 8:
        count += 1

print(count)
