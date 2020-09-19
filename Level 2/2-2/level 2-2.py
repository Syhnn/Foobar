def solution(x, y):
  result = 0
  for i in range(x):
    result = result + i + 1
  for i in range(y - 1):
    result = result + i + x
  return result

print solution(3, 4)