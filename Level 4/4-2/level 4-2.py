import math

class solver:
  def hitCheck(self, angle):
    current_pos_x = self.player_x
    current_pos_y = self.player_y

    return False

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

    trajectories = 1

    if hitCheck():
      trajectories = trajectories + 1

    return trajectories

def solution(dimensions, your_position, guard_position, distance):
  s = solver()
  s.solve(dimensions, your_position, guard_position, distance)

print solution([3,2], [1,1], [2,1], 4)