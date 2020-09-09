cache = {}

def solution(n):
  return solver(n, 1) - 1

def solver(n, p):
  result = 1
  max = (n - 1) / 2

  for i in range(p, max + 1):
    if (n - i) / 2 - i:
      if hash((n - i, i + 1)) in cache:
        result = result + cache[hash((n - i, i + 1))]
      else:
        result = result + solver(n - i, i + 1)
    else:
      result = result + 1
  
  cache[hash((n, p))] = result

  return result