n = int(input())

count = 0
time = [0, 0, 0]
three = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

for i in range((n + 1) * 60 * 60):
    if time[0] in three or time[1] in three or time[2] in three:
        count += 1
        print(time, "<")

    time[2] += 1
    if time[2] > 59:
        time[1] += 1
        time[2] = 0
        if time[1] > 59:
            time[0] += 1
            time[1] = 0

print(count)



