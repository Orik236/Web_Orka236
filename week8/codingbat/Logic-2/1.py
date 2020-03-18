def make_bricks(small, big, goal):
  goal -= min(big, goal//5)*5
  goal -= min(small, goal)
  return goal == 0
