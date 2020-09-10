def solution(l):
  if len(l) == 2:
    return 0

  result = 0
  for i in range(len(l) - 2):
    for j in range(i + 1, len(l) - 1):
      for k in range(j + 1, len(l)):
        if l[j] % l[i] == 0:
          if l[k] % l[j] == 0:
            result = result + 1
  return result
