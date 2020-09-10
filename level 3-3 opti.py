def solution(l):
  result = 0
  c = []
  for i in range(len(l)):
    c.append(0)

  for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[j] % l[i] == 0:
          c[j] = c[j] + 1
          result = result + c[j]

  return result