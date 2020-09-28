import timeit

def solution(x, y):
  result = 0
  for i in range(x):
    result = result + i + 1
  for i in range(y - 1):
    result = result + i + x
  return result

def better_solution(x, y):
  return x * (x + 1) / 2 + (x + y - 2) * (x + y - 1) / 2 - x * (x - 1) / 2

def better_solution2(x, y):
  return x + (x + y - 2) * (x + y - 1) / 2

start = timeit.default_timer()
solution(10000000, 10000000)
print timeit.default_timer() - start # around 2.25s, complexity would be... O(n^2) ?
start = timeit.default_timer()
better_solution(1000000000000000000000000000000000000, 10000000000000000000000000000000000000)
print timeit.default_timer() - start # around 1.4e-5, complexity would be O(1) i guess
start = timeit.default_timer()
better_solution2(1000000000000000000000000000000000000, 10000000000000000000000000000000000000)
print timeit.default_timer() - start # even faster and less complicated... still O(1)
