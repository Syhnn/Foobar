import math

class solver:
  def gcd(self, a, b):
    while b:
        a, b = b, a % b
    return a

  def reduce_frac(self, n, d):

    if d == 0:
      return None

    cd = self.gcd(n, d)
    n, d = n / cd, d / cd

    return n, d

  def hitCheck(self, vector):
    current_pos_x = self.player_x
    current_pos_y = self.player_y
    direction_x = self.player_x + vector[0]
    direction_y = self.player_y + vector[1]
    remaining_range = self.max_distance
    EPS = 0.00000000001

    # shooting vertically
    if vector[0] == 0:
      return self.player_x == self.guard_x and (self.guard_y > self.player_y and vector[1] > 0 or self.guard_y < self.player_y and vector[1] < 0)
    # shooting horizontally
    elif vector[1] == 0:
      return self.player_y == self.guard_y and (self.guard_x > self.player_x and vector[0] > 0 or self.guard_x < self.player_x and vector[0] < 0)
    else:
      # calculate direction equation
      a = float((current_pos_y - direction_y)) / float((current_pos_x - direction_x))
      b = current_pos_y - a * current_pos_x

      while True:
        if -EPS < a * self.guard_x + b - self.guard_y < EPS:
          # guard is on the direction line
          # check return true if direction is good and distance is good
          # otherwise continue
          if (self.guard_y > current_pos_y and vector[1] > 0 or self.guard_y < current_pos_y and vector[1] < 0) and (self.guard_x > current_pos_x and vector[0] > 0 or self.guard_x < current_pos_x and vector[0] < 0):
            d = math.sqrt(math.pow(current_pos_y - self.guard_y, 2) + math.pow(current_pos_x - self.guard_x, 2))
            return d < remaining_range
        
        x_limit = 0
        if vector[0] > 0:
          x_limit = self.map_width

        y_limit = 0
        if vector[1] > 0:
          y_limit = self.map_height

        y = a * x_limit + b
        
        if y == y_limit:
          # corner hit
          return False
        elif not 0 < y < self.map_height:
          vector[1] = -vector[1]
          newx = float(y_limit - b) / a
          d = math.sqrt(math.pow(current_pos_y - y_limit, 2) + math.pow(current_pos_x - newx, 2))
          if d < remaining_range:
            remaining_range = remaining_range - d
            current_pos_y = y_limit
            current_pos_x = newx
          else:
            return False
        else:
          vector[0] = -vector[0]
          newy = a * x_limit + b
          d = math.sqrt(math.pow(current_pos_y - newy, 2) + math.pow(current_pos_x - x_limit, 2))
          if d < remaining_range:
            remaining_range = remaining_range - d
            current_pos_y = newy
            current_pos_x = x_limit
          else:
            return False

        a = -a
        b = current_pos_y - a * current_pos_x

  def solve(self, dimensions, your_position, guard_position, distance):
    self.player_x = your_position[0]
    self.player_y = your_position[1]
    self.guard_x = guard_position[0]
    self.guard_y = guard_position[1]
    self.map_width = dimensions[0]
    self.map_height = dimensions[1]
    self.max_distance = distance
    self.distance = math.sqrt(math.pow(self.guard_y - self.player_y, 2) + math.pow(self.guard_x - self.player_x, 2))

    if self.distance > self.max_distance:
      return 0
    elif self.distance == self.max_distance:
      return 1

    trajectories = 0

    test = 100
    directions = []
    for x in range(1, test):
      for y in range(1, test):
        if x == 0 or y == 0:
          continue

        if not x&1 and not y&1:
          continue

        a, b = self.reduce_frac(x, y)

        if not [a, b] in directions:
          directions.append([a, b])
          directions.append([a, -b])
          directions.append([-a, b])
          directions.append([-a, -b])
          
    directions.append([ 1,  0])
    directions.append([-1,  0])
    directions.append([ 0,  1])
    directions.append([ 0, -1])

    for dir in directions:
      if self.hitCheck(dir):
        trajectories = trajectories + 1

    return trajectories

def solution(dimensions, your_position, guard_position, distance):
  s = solver()
  return s.solve(dimensions, your_position, guard_position, distance)

print solution([3,2], [1,1], [2,1], 4)