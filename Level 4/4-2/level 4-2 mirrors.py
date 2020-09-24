import math

def solution(dimensions, your_position, guard_position, distance):
  player_x, player_y = your_position
  guard_x, guard_y = guard_position
  map_width, map_height = dimensions
  max_distance = distance

  hit_count = 0
  vertical_case = False
  horizontal_case = False
  
  mirror_players = dict()
  mirror_guards = dict()  
  hit_list = []

  distance = math.sqrt(math.pow(guard_x - player_x, 2) + math.pow(guard_y - player_y, 2))

  if distance > max_distance:
    return 0
  elif distance == max_distance:
    return 1

  angle = math.atan2(float(guard_y - player_y), float(guard_x - player_x))
  hit_list.append(angle)
  hit_count = hit_count + 1

  if player_x == guard_x:
    horizontal_case = True
  if player_y == guard_y:
    vertical_case = True
  
  i_limit = max_distance / map_width + 1
  j_limit = max_distance / map_height + 1

  for x in range(- i_limit, i_limit + 1):
    for y in range(- j_limit, j_limit + 1):

      if horizontal_case and x == 0 or vertical_case and y == 0 or x == y == 0:
        continue
      px = (x / 2 * player_x * 2) + ((x + 1) / 2 * (map_width - player_x) * 2)
      py = (y / 2 * player_y * 2) + ((y + 1) / 2 * (map_height - player_y) * 2)
      distance = math.sqrt(math.pow(px, 2) + math.pow(py, 2))
      if distance <= max_distance:
        angle = math.atan2(float(py), float(px))
        test = angle in mirror_players
        if not test or test and distance < mirror_players[angle]:
          mirror_players[angle] = distance

      gx = guard_x - player_x + (x / 2 * guard_x * 2) + ((x + 1) / 2 * (map_width  - guard_x) * 2)
      gy = guard_y - player_y + (y / 2 * guard_y * 2) + ((y + 1) / 2 * (map_height - guard_y) * 2)
      distance = math.sqrt(math.pow(gx, 2) + math.pow(gy, 2))
      if distance <= max_distance:
        angle = math.atan2(float(gy), float(gx))
        test = angle in mirror_guards
        if not test or test and distance < mirror_guards[angle]:
          mirror_guards[angle] = distance

  for ga in mirror_guards:
    if ga in mirror_players and mirror_players[ga] < mirror_guards[ga]:
      continue

    if not ga in hit_list:
      hit_list.append(ga)
      hit_count = hit_count + 1

  return hit_count

print solution([3,2], [1,1], [2,1], 4)
print solution([2,5], [1,2], [1,4], 11)
print solution([300,275], [150,150], [185,100], 500)
