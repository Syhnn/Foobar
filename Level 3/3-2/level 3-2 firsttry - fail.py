import timeit

def steps(n):
  c = 1
  while True:
    n = n - c
    if n < 0:
      return c - 1
    c = c + 1

def brickCount(n):
  count = 0
  for i in range(n):
    count = count + i + 1
  return count

def twoStepStair(n, m):
  result = 0
  s1 = n - 1
  s2 = 1
  if s1 >= m:
    s1 = m - 1
    s2 = n - s1
  while s1 > s2:
    result = result + 1
    s1 = s1 - 1
    s2 = s2 + 1
  return result

def fixedStairSolver(n, m, c):
  result = 0

  if c > 2:
    remaining = n - brickCount(c)
    if remaining == 0:
      result = result + 1
    else:
      for rest in range(remaining + 1):
          if c + remaining - rest < m:
            result = result + fixedStairSolver(brickCount(c - 1) + rest, c + remaining - rest, c - 1)
  else:
    result = result + twoStepStair(n, m)
  
  return result

def stairsolver(n, m):
  maxstep = steps(n)
  result = 0

  for stepcount in range(2, maxstep + 1):
    result = result + fixedStairSolver(n, m, stepcount)
  
  return result

def solution(n):
  return stairsolver(n, 200)
