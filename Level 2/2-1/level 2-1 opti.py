import math

def solution(h, q):
  result = []
  parents = [3, 3] # base for tree of height 2

  # if tree is made of only one node answer is always -1
  if h == 1:
    for i in q:
      result.append(-1)
    return result

  # if tree height is at least 3, build the rest of the sequence
  elif h >= 3:
    for i in range (3, h+1):
      top = int(math.pow(2, i))-1
      newparents = [top]
      for value in parents:
        newparents.append(int(value + math.pow(2, i-1)-1))
      newparents.append(top)
      parents = parents + newparents

  # add root node value
  parents.append(-1)
    
  for i in q:
    result.append(parents[i-1])
    
  return result

print solution(1, [1, 1, 1])
print solution(2, [1, 2, 3])
print solution(3, [1, 4, 7])
print solution(5, [19, 14, 28])

