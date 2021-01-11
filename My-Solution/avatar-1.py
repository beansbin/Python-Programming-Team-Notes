n = int(input())
arr = input().split()

location = [1, 1]

for i in range(len(arr)):
  if arr[i] == 'L' and location[0]-1 >= 1:
    location[0]-=1
  elif arr[i] == 'R' and location[0]+1 <= n:
    location[0]+=1
  elif arr[i] == 'U' and location[1]-1 >= 1:
    location[1]-=1
  elif arr[i] == 'D' and location[1]+1 <= n:
    location[1]+=1

print(location[1], location[0]) # Y, X
