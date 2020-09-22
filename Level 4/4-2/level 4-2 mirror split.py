import math

def obstacleCheck(list, target, fact):
  for obs in list:
    if (obs == target or
        not 0 <= obs[0] <= target[0] and not 0 >= obs[0] >= target[0] or
        not 0 <= obs[1] <= target[1] and not 0 >= obs[1] >= target[1]):
      continue
    if fact * obs[0] == obs[1]:
      return False
  return True

def solution(dimensions, your_position, guard_position, distance):
  player_x = your_position[0]
  player_y = your_position[1]
  guard_x = guard_position[0]
  guard_y = guard_position[1]

  map_width = dimensions[0]
  map_height = dimensions[1]
  max_distance = distance
  hit_count = 0
  vertical_case = False
  
  mirror_players = []
  mirror_guards = []
  mirror_corners = []
  
  mptr = []
  mptl = []
  mpbr = []
  mpbl = []
  mgtr = []
  mgtl = []
  mgbr = []
  mgbl = []
  mctr = []
  mctl = []
  mcbr = []
  mcbl = []

  distance = math.sqrt(math.pow(guard_x - player_x, 2) + math.pow(guard_y - player_y, 2))

  if distance > max_distance:
    return 0
  elif distance == max_distance:
    return 1
  
  mirror_guards.append([guard_x - player_x, guard_y - player_y])
  mgtr.append([guard_x - player_x, guard_y - player_y])
  
  i_limit = max_distance / map_width + 1
  j_limit = max_distance / map_height + 1

  for x in range(- i_limit, i_limit + 1):
    for y in range(- j_limit, j_limit + 1):
      if not x == - i_limit and not y == - j_limit:
        #mirror_corners.append([x * map_width - player_x, y * map_height - player_y])
        if x >= 0:
          if y >= 0:
            mctr.append([x * map_width - player_x, y * map_height - player_y])
          else:
            mcbr.append([x * map_width - player_x, y * map_height - player_y])
        else:
          if y >= 0:
            mctl.append([x * map_width - player_x, y * map_height - player_y])
          else:
            mcbl.append([x * map_width - player_x, y * map_height - player_y])

      if x == y == 0:
        continue
      
      if x >= 0:
        if y >= 0:
          mptr.append([(x / 2 * player_x * 2) + ((x + 1) / 2 * (map_width - player_x) * 2),
                       (y / 2 * player_y * 2) + ((y + 1) / 2 * (map_height - player_y) * 2)])
          mgtr.append([guard_x - player_x + (x / 2 * guard_x * 2) + ((x + 1) / 2 * (map_width - guard_x ) * 2),
                       guard_y - player_y + (y / 2 * guard_y * 2) + ((y + 1) / 2 * (map_height - guard_y) * 2)])
        else:
          mpbr.append([(x / 2 * player_x * 2) + ((x + 1) / 2 * (map_width - player_x) * 2),
                       (y / 2 * player_y * 2) + ((y + 1) / 2 * (map_height - player_y) * 2)])
          mgbr.append([guard_x - player_x + (x / 2 * guard_x * 2) + ((x + 1) / 2 * (map_width - guard_x ) * 2),
                       guard_y - player_y + (y / 2 * guard_y * 2) + ((y + 1) / 2 * (map_height - guard_y) * 2)])
      else:
        if y >= 0:
          mptl.append([(x / 2 * player_x * 2) + ((x + 1) / 2 * (map_width - player_x) * 2),
                       (y / 2 * player_y * 2) + ((y + 1) / 2 * (map_height - player_y) * 2)])
          mgtl.append([guard_x - player_x + (x / 2 * guard_x * 2) + ((x + 1) / 2 * (map_width - guard_x ) * 2),
                       guard_y - player_y + (y / 2 * guard_y * 2) + ((y + 1) / 2 * (map_height - guard_y) * 2)])
        else:
          mpbl.append([(x / 2 * player_x * 2) + ((x + 1) / 2 * (map_width - player_x) * 2),
                       (y / 2 * player_y * 2) + ((y + 1) / 2 * (map_height - player_y) * 2)])
          mgbl.append([guard_x - player_x + (x / 2 * guard_x * 2) + ((x + 1) / 2 * (map_width - guard_x ) * 2),
                       guard_y - player_y + (y / 2 * guard_y * 2) + ((y + 1) / 2 * (map_height - guard_y) * 2)])

      #mirror_players.append([(x / 2 * player_x * 2) + ((x + 1) / 2 * (map_width - player_x) * 2),
      #                       (y / 2 * player_y * 2) + ((y + 1) / 2 * (map_height - player_y) * 2)])
      mirror_guards.append([guard_x - player_x + (x / 2 * guard_x * 2) + ((x + 1) / 2 * (map_width - guard_x ) * 2),
                            guard_y - player_y + (y / 2 * guard_y * 2) + ((y + 1) / 2 * (map_height - guard_y) * 2)])

  for guard in mirror_guards:
    distance = math.sqrt(math.pow(guard[0], 2) + math.pow(guard[1], 2))
    if distance < max_distance:
      try:
        a = float((guard[1])) / float((guard[0]))
      except ZeroDivisionError:
        if not vertical_case:
          hit_count = hit_count + 1
          vertical_case = True
        continue
      if ((guard[0] >= 0 and guard[1] >= 0 and (not obstacleCheck(mgtr, guard, a) or not obstacleCheck(mptr, guard, a) or not obstacleCheck(mctr, guard, a))) or 
          (guard[0] >= 0 and guard[1] <  0 and (not obstacleCheck(mgbr, guard, a) or not obstacleCheck(mpbr, guard, a) or not obstacleCheck(mcbr, guard, a))) or 
          (guard[0] <  0 and guard[1] >= 0 and (not obstacleCheck(mgtl, guard, a) or not obstacleCheck(mptl, guard, a) or not obstacleCheck(mctl, guard, a))) or 
          (guard[0] <  0 and guard[1] <  0 and (not obstacleCheck(mgbl, guard, a) or not obstacleCheck(mpbl, guard, a) or not obstacleCheck(mcbl, guard, a)))):
        continue
      hit_count = hit_count + 1

  return hit_count

print solution([4,4], [3,2], [2,2], 8)
