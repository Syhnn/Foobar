class solver:
  def displayGraph(self):
    print "Adjacency Matrix:"
    for room in self.g:
      print room

  def displayResidualFlow(self):
    print "Residual Flow Matrix:"
    for room in self.residual_flow:
      print room

  def explore(self, node, flow, path):
    rf = 0
    if node in self.t:
      rf = flow - self.residual_flow[path[-1]][node]
      self.residual_flow[path[-1]][node] = self.residual_flow[path[-1]][node] + rf
      return rf

    for i, f in enumerate(self.g[node]):
      if flow - rf == 0:
        break

      if f != 0 and self.residual_flow[node][i] < f:
        if not i in path:
          rf = rf + self.explore(i, min(flow, f), path[:] + [node])

    self.residual_flow[path[-1]][node] = self.residual_flow[path[-1]][node] + rf
    return rf

  def solve(self, entrances, exits, path):
    self.s = entrances
    self.t = exits
    self.g = path
    self.residual_flow = [[0 for i in range(len(path))] for j in range(len(path))]

    for e in entrances:
      for i, f in enumerate(self.g[e]):
        if f != 0:
          self.explore(i, f, [e])

    result = 0
    for t in self.t:
        for i in range(len(path)):
            result = result + self.residual_flow[i][t]

    return result

def solution(entrances, exits, path):
  s = solver()
  return s.solve(entrances, exits, path)

print solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])